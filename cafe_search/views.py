from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count, Q
from functools import reduce
import operator
from cafe.models import Cafe, CafeImage, Tag
from accounts.models import Profile
from cafe_select.models import Review
from django.contrib import messages
from dotenv import load_dotenv
import os


# Create your views here.
def search_before(request):
    return render(request, "search_before.html")

def search_after(request):
    user=get_object_or_404(User, pk=request.user.id)
    if request.method=='POST':
        if request.POST:
            if len(request.POST.getlist('s_mood_tag')) > 3 :
                messages.warning(request, "분위기 태그는 최대 3개까지만 선택 가능합니다.")
                return redirect('cafe_search:search_before')
            elif len(request.POST.getlist('s_mood_tag'))==0:
                messages.error(request, "분위기 태그를 최소 1개 이상 선택해주세요!")
                return redirect('cafe_search:search_before')
            else:
                searched = ','.join(request.POST.getlist('s_mood_tag'))
        return redirect(f'{reverse("cafe_search:search_after")}?searched={searched}')
    else:
        searched_term = request.GET.get('searched', '')
        searched=searched_term.split(',')
        search_tag=[]
        
        for search in searched:
            tag_obj = Tag.objects.filter(code=search).first()
            if tag_obj:
                search_tag.append(tag_obj.code)

        if not search_tag:
            cafes = Cafe.objects.none()
        else:
            # 하나라도 매칭되는 것들 필터
            tag_query = Q()
            for tag in search_tag:
                tag_query |= Q(cafe_most_tags__code=tag)

            # 겹치는 태그 수를 카운트하여 정렬
            cafes = (
                Cafe.objects
                .filter(tag_query)
                .annotate(matched_tags=Count('cafe_most_tags', filter=Q(cafe_most_tags__code__in=search_tag)))
                .order_by('-matched_tags')  # 많이 겹치는 순
                .distinct()
            )
        
        cafe_list=[]
        
        for cafe in cafes:
            cafeimage=CafeImage.objects.filter(cafe_id=cafe.id).first()
            cafe_list.append((cafe, cafeimage))
            
        search_tags=[]
        for s in searched:
            se=Tag.objects.filter(code=s).first()
            search_tags.append(se)
            
        context = {
            'cafe_list':cafe_list,
            'search_tags' : search_tags
        }
        return render(request, "search_after.html", context)
    
def search_detail(request, cafe_id):
    user=get_object_or_404(User, pk=request.user.id)
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    cafeimage=CafeImage.objects.filter(cafe=cafe).first()
    reviews_all=Review.objects.filter(cafe=cafe)
    
    reviews=[(Profile.objects.get(user=review.user),review) for review in reviews_all]
    
    tag_codes = cafe.cafe_most_tags.values_list('code', flat=True)
    
    tags=[]
    for t in tag_codes:
        tags.append(Tag.objects.filter(code=t).first())
    
    load_dotenv()
    
    myjskey=os.getenv('JS_KEY')
    
    context={
        'cafe' : cafe,
        'cafe_id' : cafe_id,
        'cafeimage' : cafeimage,
        'reviews' : reviews,
        'myjskey':myjskey,
        'tags' : tags
    }
    
    return render(request, "search_detail.html", context)

