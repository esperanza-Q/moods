from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cafe, CafeImage
from rest_api.api import get_location
from django.db.models import Count
from cafe_select.models import Mood_tags

# Create your views here.
def cafeadd(request):
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
            cafe_y=cafe_y
        )
        
        cafeimage = request.FILES.get('cafeimage')  # 파일이 있으면 가져오기
        if cafeimage:
            # CafeImage 객체 생성 및 연결
            CafeImage.objects.create(
                cafe=cafe,  # 생성된 cafe 객체 연결
                cafeimage=cafeimage
            )
            
        return redirect('home:home')
    
    return render(request, 'test_cafe_add.html')  # GET 요청 시 폼을 가진 페이지 반환

def update_top_tags(cafe):
    tag_counts = (
        Mood_tags.objects.filter(cafe=cafe)
        .values('tags')  # M2M이므로 tags
        .annotate(count=Count('tags'))
        .order_by('-count')[:3]
    )
    top_tags = [item['tags'] for item in tag_counts]
    cafe.cafe_most_tags.set(top_tags)