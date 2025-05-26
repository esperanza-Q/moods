from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Q
from django.urls import reverse
from cafe.models import Cafe, CafeImage, Tag
from django.http import HttpResponseBadRequest
from .models import Review, Mood_tags
from django.contrib.auth.models import User
from dotenv import load_dotenv
import os
from django.contrib import messages
import heapq
from django.views.decorators.http import require_POST
from cafe.views import update_top_tags
from cafe_select.models import Mood_tags


# Create your views here.
def select_before(request):
    return render(request, 'select_before.html')

def select_searched(request):
    # if request.method=='POST':
    #     select_searchbar=request.POST.get('select_searchbar','')
    #     return redirect(f'{reverse("cafe_select:select_searched", kwargs={"request.user.id": request.user.id})}?searched={select_searchbar}')
    # else:
    select_searchbar=request.GET.get('select_searchbar','')
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
        # if count == 0:
        #     continue
        cafeimage=CafeImage.objects.filter(cafe_id=cafe.id).first()
        
        cafe_with_count.append((cafe, count, cafeimage))
            
    cafe_with_count.sort(key = lambda x:x[1], reverse=True)
    sorted_cafe=[(cafe,cafeimage) for cafe,count,cafeimage in cafe_with_count]
        
    return render(request, 'select_after.html', {'cafe_list':sorted_cafe})
    
def select_detail(request, cafe_id):
    cafe = get_object_or_404(Cafe, pk =cafe_id)
    cafeimage=CafeImage.objects.filter(cafe_id=cafe_id).first()
    
    existing_review = Review.objects.filter(user=request.user, cafe=cafe).exists()
    existing_mood_tag = Mood_tags.objects.filter(user=request.user, cafe=cafe).exists()

    load_dotenv()

    myjskey=os.getenv('JS_KEY')
    
    if existing_review:
        review_already='Y'
    else:
        review_already='N'
        
    if existing_mood_tag:
        mood_already='Y'
    else:
        mood_already='N'

    context = {
        'cafe': cafe,
        'cafe_id':cafe.id,
        'cafeimage':cafeimage,
        'review_already':review_already,
        'mood_already':mood_already,
        'myjskey':myjskey
    }
    return render(request, 'select_detail.html', context)

def review_form(request):
    return render(request, 'review_form.html')

def review(request, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=request.user.id)
    
    if request.method=="POST":
        review_image=request.FILES.get('review_image')
        review_content=request.POST.get('review_content','')
        
        Review.objects.create(
            cafe=cafe,
            user=user,
            review_image=review_image,
            review_content=review_content,
        )
        return redirect('cafe_select:select_detail', cafe_id=cafe_id)
    else:
        context={
            'cafe_id':cafe_id
        }
        return render(request, 'test_review_write.html', context)

def delete_review(request, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=request.user.id)
    
    Review.objects.filter(user=user, cafe=cafe).delete()
    
    return redirect('cafe_select:select_detail', cafe_id=cafe_id)

@require_POST  
def select_tag(request, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=request.user.id)
    if request.POST:
        select = request.POST.getlist('mood_tag')
        if len(select) > 3 :
            messages.warning(request, "분위기 태그는 최대 3개까지만 선택 가능합니다.")
            return redirect('cafe_select:select_detail', cafe_id=cafe_id)
        elif len(select)==0:
            messages.error(request, "분위기 태그를 최소 1개 이상 선택해주세요!")
            return redirect('cafe_select:select_detail', cafe_id=cafe_id)
        else:
            if select:
                mood_entry = Mood_tags.objects.create(user=user, cafe=cafe)
                # for tag_code in select:
                #     tag = Tag.objects.filter(code=tag_code).first()
                #     if tag:
                #         mood_entry.tags.add(tag)
                # mood_entry.save()
            
                mood_entry.save()
                for tag_code in select:
                    tag = Tag.objects.filter(code=tag_code).first()
                    if tag:
                        mood_entry.tags.add(tag)
                        update_top_tags(cafe)
                        
                print(select)  # 리스트 확인
                print(tag_code, tag)  # 각 tag가 있는지 확인
            
            return redirect('cafe_select:select_detail', cafe_id=cafe_id)
    return redirect('cafe_select:select_detail', cafe_id=cafe_id)

def reselect_tag(request, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=request.user.id)
    
    Mood_tags.objects.filter(user=user, cafe=cafe).delete()
    update_top_tags(cafe)
    
    return redirect('cafe_select:select_detail', cafe_id=cafe_id)




# @require_POST
# def select_tag(request, user_id, cafe_id):
#     user = get_object_or_404(User, pk=user_id)
#     cafe = get_object_or_404(Cafe, pk=cafe_id)
    
#     # 기존에 투표한 기록이 있으면 삭제 (혹은 업데이트 로직)
#     Mood_tags.objects.filter(user=user, cafe=cafe).delete()

#     # 선택된 태그 코드 리스트 (checkbox 값들)
#     selected_tags = request.POST.getlist('mood_tag')

#     if selected_tags:
#         mood_entry = Mood_tags.objects.create(user=user, cafe=cafe)
#         # 코드 기반으로 Tag 객체 찾아서 연결
#         for tag_code in selected_tags:
#             tag = Tag.objects.filter(code=tag_code).first()
#             if tag:
#                 mood_entry.tags.add(tag)
#         mood_entry.save()

#     return redirect('some_result_page_or_detail', cafe_id=cafe_id)

# def most_tag(cafe_id):
#     cafe=get_object_or_404(Cafe, pk=cafe_id)
#     tags=Mood_tags.objects.filter(cafe=cafe)
#     tagcount_dic={"coffee":0,"refined":0,"together":0,"dessert":0,"clean":0,"study":0,"cozy":0,"big":0,"alone":0,"cuty":0,"always":0,"picture":0}
#     for tag in tags:
#         moodtag=tag.tags
#         for t in moodtag:
#             tagcount_dic[t]+=1
#     max3=heapq.nlargest(3, tagcount_dic, key = tagcount_dic.get)
#     Cafe.objects.filter(id=cafe_id).update(cafe_most_tags = max3)