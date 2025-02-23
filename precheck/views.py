from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Checkpost, CheckImage
from .forms import Checkpostform
from django.urls import reverse
from accounts.models import Profile

# Create your views here.
def precheck(request, user_id):
    if Checkpost.objects.filter(user=request.user).exists():  # 이미 인증글이 있으면
        checkpost = get_object_or_404(Checkpost, user_id=user_id)

        return redirect(reverse('precheck:precheck_A', kwargs={'user_id': user_id, 'checkpost_id': checkpost.id}))  # 인증글이 있으면 다른 페이지로 리다이렉트
    else:
        return redirect('precheck:precheck_B', user_id)

def precheck_A(request, user_id, checkpost_id):
    profile=get_object_or_404(Profile, user_id=user_id)
    checkpost = get_object_or_404(Checkpost, user_id=user_id)
    checkimage=CheckImage.objects.filter(checkpost=checkpost).first()
    
    context = {
        'checkpost': checkpost,
        'checkimage': checkimage,
        'profile':profile
    }
    return render(request, 'test_pre_check_A.html', context)

def precheck_B(request, user_id):
    profile=get_object_or_404(Profile, user_id=user_id)
    if request.method == 'POST':
        form = Checkpostform(request.POST, request.FILES)
        if form.is_valid():
            checkpost = form.save(commit=False)
            checkpost.user = request.user  # 포스트 작성자 지정
            checkpost.verified_check = profile
            checkpost.save()  # 포스트 저장

            # 이미지 파일이 있다면 저장
            checkimage = request.FILES.get('checkimage')  # 하나의 이미지만 가져오기
            if checkimage:
                # CheckImage 객체 생성
                CheckImage.objects.create(checkpost=checkpost, checkimage=checkimage)
                
            
            return redirect(reverse('precheck:precheck_A', kwargs={'user_id': user_id, 'checkpost_id': checkpost.id}), profile) # 인증글 작성 후 precheck_A로 리디렉션
        else:
            # 폼이 유효하지 않으면 precheck로 리디렉션
            print(form.errors)
            return redirect('precheck:test')
    else:
        form = Checkpostform()  # GET 요청일 경우 새 폼을 생성
        return render(request, 'test_pre_check.html', {'user_id': user_id, 'form': form, 'profile':profile})


def precheck_delete(request, user_id, checkpost_id):
    checkpost = get_object_or_404(Checkpost, id=checkpost_id)
    checkpost.delete()
    return redirect('precheck:precheck', user_id)
    
def test(request):
    return render(request, 'test.html')