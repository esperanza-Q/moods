from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Count, Q
from functools import reduce
import operator
from cafe.models import Cafe, CafeImage
from accounts.models import Profile
from cafe_select.models import Review
from django.contrib import messages
from dotenv import load_dotenv
import os


# Create your views here.
def search_before(request, user_id):
    return render(request, "test_search_before.html", {'user_id':user_id})

def search_after(request, user_id):
    user=get_object_or_404(User, pk=user_id)
    if request.method=='POST':
        if request.POST:
            if len(request.POST.getlist('s_mood_tag')) > 3 :
                messages.warning(request, "분위기 태그는 최대 3개까지만 선택 가능합니다.")
                return redirect('cafe_search:search_before', user_id=user_id)
            elif len(request.POST.getlist('s_mood_tag'))==0:
                messages.error(request, "분위기 태그를 최소 1개 이상 선택해주세요!")
                return redirect('cafe_search:search_before', user_id=user_id)
            else:
                searched = ','.join(request.POST.getlist('s_mood_tag'))
            
        return redirect(f'{reverse("cafe_search:search_after", kwargs={"user_id": user_id})}?searched={searched}')
    else:
        searched_term = request.GET.get('searched', '')
        searched=searched_term.split(',')
        
        query_list = [Q(cafe_most_tags__contains=[term]) for term in searched]
        final_query = reduce(operator.and_, query_list)
        cafes = Cafe.objects.filter(final_query)
        
        cafe_list=[]
        
        for cafe in cafes:
            cafeimage=CafeImage.objects.filter(cafe_id=cafe.id).first()
            cafe_list.append((cafe, cafeimage))
        context = {
            'cafe_list':cafe_list,
            'user_id' : user_id,
        }
        return render(request, "test_search_after.html", context)
    
def search_detail(request, user_id, cafe_id):
    user=get_object_or_404(User, pk=user_id)
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    cafeimage=CafeImage.objects.filter(cafe=cafe).first()
    reviews_all=Review.objects.filter(cafe=cafe)
    
    reviews=[(Profile.objects.get(user=review.user),review) for review in reviews_all]
    
    tagname_dic={"coffee":"커피가 맛있는","refined":"세련된","together":"단체모임하기 좋은","dessert":"디저트가 맛있는","clean":"깔끔한","study":"카공하기 좋은","cozy":"포근한","big":"넓은","alone":"혼자 있기 좋은","cuty":"아기자기한","always":"24시간 영업하는","picture":"사진 찍기 좋은"}
    tags=[tagname_dic[tag] for tag in cafe.cafe_most_tags]
    
    load_dotenv()
    
    myjskey=os.getenv('JS_KEY')
    
    context={
        'user_id' : user_id,
        'cafe' : cafe,
        'cafe_id' : cafe_id,
        'cafeimage' : cafeimage,
        'reviews' : reviews,
        'myjskey':myjskey,
        'tags' : tags
    }
    
    return render(request, "test_search_detail.html", context)