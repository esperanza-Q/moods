from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cafe, CafeImage
from rest_api.api import get_location

# Create your views here.
def cafeadd(request, user_id):
    if not request.user.is_superuser:
        return redirect('home:prehome')
    
    if request.method=='POST':
        cafename = request.POST['cafename']
        cafelocation = request.POST['cafelocation']
        cafeinfo = request.POST['cafeinfo']
        cafeID = request.POST['cafeID']
        
        cafe_x, cafe_y = get_location(cafelocation)
    
        cafe = Cafe.objects.create(
            cafename=cafename,
            cafelocations=cafelocation,
            cafeinfo=cafeinfo,
            cafeID=cafeID,
            cafe_x=cafe_x,
            cafe_y=cafe_y,
            cafe_most_tags=[],
        )
        
        cafeimage = request.FILES.get('cafeimage')  # 파일이 있으면 가져오기
        if cafeimage:
            # CafeImage 객체 생성 및 연결
            CafeImage.objects.create(
                cafe=cafe,  # 생성된 cafe 객체 연결
                cafeimage=cafeimage
            )
            
        return redirect('home:home', user_id)
    
    return render(request, 'test_cafe_add.html', {'user_id':user_id})  # GET 요청 시 폼을 가진 페이지 반환