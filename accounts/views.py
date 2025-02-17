from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse


# Create your views here.
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        nickname = request.POST['nickname']
        
        user = None
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "이미 사용 중인 아이디입니다!")
            return redirect('accounts:signup')
        
        if password1==password2:
            user=User.objects.create_user(
                username = username,
                password = password1,
                email=email
            )
            user.is_active = True  # 계정 비활성화 (필요 시)
            user.save()
            
            profile=Profile.objects.create(
                user=user,
                nickname=nickname
            )
            
            auth.login(request, user)
            
            if user.profile.user_type == 'verified':
                return redirect('home:home', user.id)  # 인증된 유저
            else:
                return redirect('precheck:precheck', user.id)  # 인증 전 유저
            
        else:
            messages.error(request, 'PW와 Re-PW가 일치하지 않습니다!')
            return redirect('accounts:signup')
    return render(request, 'test_signup.html')

def login(request):
    if request.method=='POST':
        u_username=request.POST['u_username']
        u_password=request.POST['u_password']
        user=authenticate(request, username=u_username, password=u_password)
        if user is not None:
            auth.login(request, user)
            if user.profile.user_type == 'verified':
                return redirect('home:home', user.id)  # 인증된 유저
            else:
                # return redirect(reverse('accounts:precheck', kwargs={'user_id': user.id}))  # 인증 전 유저
                return redirect('precheck:precheck', user.id)
        else:
            messages.error(request, '아이디 혹은 비밀번호가 일치하지 않습니다!')
            return redirect('accounts:login')
    return render(request, 'test_login.html')

def logout(request):
    auth.logout(request)
    return redirect('home:prehome')