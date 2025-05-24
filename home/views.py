from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    
    user = get_object_or_404(User, pk=request.user.id)
    profile=get_object_or_404(Profile, user=user)
    
    if request.user.profile.user_type == 'guest':
        return redirect('precheck:precheck', user.id)
    else:
        
        
        context = {
            'profile':profile
            }
        return render(request, 'home.html', context)

def prehome(request):
    return render(request, 'prehome.html')

def firstpage(request):
    if request.user.is_authenticated:
        return redirect('home:home')
    else:
        return redirect('home:prehome')
    