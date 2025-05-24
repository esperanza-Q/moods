from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm
# Create your views here.

@login_required
def mypage(request):
    user = get_object_or_404(User, pk=request.user.id)
    profile=get_object_or_404(Profile, user=user)
    
    context={
        'profile':profile,
        'user':user,
    }
    return render(request, 'test_mypage.html', context)

def profile_update(request):
    user = get_object_or_404(User, pk=request.user.id)
    profile=get_object_or_404(Profile, user=user)
    
    if request.method == 'GET':
        # profile_update_form = ProfileForm(instance=profile)
        complete=0
        context={
            # 'profile_update_from':profile_update_form,
            'profile':profile,
            'complete':complete,
        }
        return render(request, 'test_mypage_update.html', context)
    else:
        # profile_update_form=ProfileForm(request.POST,request.FILES, instance=profile)
        # if profile_update_form.is_valid():
            # profile_update_form.save()
        nickname=request.POST["upd_nickname"]

        profile.nickname=nickname
        profile.save()

        return redirect('mypage:mypage')
    