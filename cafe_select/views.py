from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.urls import reverse
from cafe.models import Cafe, CafeImage
from django.http import HttpResponseBadRequest
from .models import Review
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os



# Create your views here.
def select_before(request, user_id):
    return render(request, 'select_before.html', {'user_id':user_id})

def select_searched(request, user_id):
    if request.method=='POST':
        select_searchbar=request.POST.get('select_searchbar','')
        return redirect(f'{reverse("cafe_select:select_searched", kwargs={"user_id": user_id})}?searched={select_searchbar}')
    else:
        select_searchbar=request.GET.get('searched','')
        search_terms=set(select_searchbar.replace(',',' ').split())
        search_terms=set(term.lower() for term in search_terms )

        query=Q()
        
        for term in search_terms:
            query |= Q(cafename__icontains=term) | Q(cafelocations__icontains=term)
            
        cafes=Cafe.objects.filter(query)

        cafe_with_count = []
        
        for cafe in cafes:
            # 카페 이름과 위치를 소문자로 처리
            cafe_name = cafe.cafename.lower()
            cafe_locations = cafe.cafelocations.lower()
            
            # cafeimage=CafeImage.objects.filter(cafe=cafe).first()
            # print(cafeimage)
            
            # 검색어에 대해 각 카페에서 몇 번 나오는지 계산
            count = sum(cafe_name.count(term) + cafe_locations.count(term) for term in search_terms)
            cafeimage=CafeImage.objects.filter(cafe_id=cafe.id).first()
            
            cafe_with_count.append((cafe, count, cafeimage))
            
        cafe_with_count.sort(key = lambda x:x[1], reverse=True)
        sorted_cafe=[(cafe,cafeimage) for cafe,count,cafeimage in cafe_with_count]
        
        
        
        return render(request, 'test_select_after.html', {'user_id':user_id, 'cafe_list':sorted_cafe})
    
def select_detail(request, user_id, cafe_id):
    cafe = get_object_or_404(Cafe, pk =cafe_id)
    cafeimage=CafeImage.objects.filter(cafe_id=cafe_id).first()
    
    existing_review = Review.objects.filter(user=request.user, cafe=cafe).exists()
    
    load_dotenv()

    myjskey=os.getenv('JS_KEY')
    
    if existing_review:
        already='Y'
    else:
        already='N'

    context = {
        'cafe': cafe,
        'cafe_id':cafe.id,
        'user_id': user_id,
        'cafeimage':cafeimage,
        'already':already,
        'myjskey':myjskey
    }
    return render(request, 'test_select_detail.html', context)

def review_form(request):
    return render(request, 'review_form.html')

def review(request, user_id, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=user_id)
    
    if request.method=="POST":
        review_image=request.FILES.get('review_image')
        review_content=request.POST.get('review_content','')
        
        Review.objects.create(
            cafe=cafe,
            user=user,
            review_image=review_image,
            review_content=review_content,
        )
        return redirect('cafe_select:select_detail', user_id=user_id, cafe_id=cafe_id)
    else:
        context={
            'user_id':user_id,
            'cafe_id':cafe_id
        }
        return render(request, 'test_review_write.html', context)