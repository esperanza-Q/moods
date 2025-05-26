from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from cafe_select.models import Review, Mood_tags
from cafe.models import Cafe, CafeImage, Tag
from django.db.models import Count, Q, Case, When
from collections import Counter
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
    return render(request, 'mypage.html', context)

def profile_update(request):
    user = get_object_or_404(User, pk=request.user.id)
    profile=get_object_or_404(Profile, user=user)
        
    nickname=request.POST["upd_nickname"]

    p_image = request.FILES.get('new_profile')

        
    if p_image:
        profile.profile_image=p_image
    profile.nickname=nickname
    profile.save()

    return redirect('mypage:mypage')
    
def my_review(request):
    reviews=Review.objects.filter(user_id=request.user.id)
    reviewCafe=[]
    for review in reviews:
        reviewCafe.append((review, Cafe.objects.filter(pk=review.cafe_id).first()))
    return render(request, 'mypage_reviewlist.html', {'reviewCafe':reviewCafe})

def delete_myreview(request, cafe_id):
    cafe=get_object_or_404(Cafe, pk=cafe_id)
    user=get_object_or_404(User, pk=request.user.id)
    
    Review.objects.filter(user=user, cafe=cafe).delete()
    
    return redirect('mypage:my_review')


def my_mood(request):
    return render(request, 'mypage_moodselectsearch.html')

def my_mood_cafe(request):
    user = get_object_or_404(User, pk=request.user.id)

    if request.method == 'POST':
        if request.POST:
            selected_tags = request.POST.getlist('my_mood_tag')
            if len(selected_tags) > 3:
                messages.warning(request, "분위기 태그는 최대 3개까지만 선택 가능합니다.")
                return redirect('mypage:my_mood')
            elif len(selected_tags) == 0:
                messages.error(request, "분위기 태그를 최소 1개 이상 선택해주세요!")
                return redirect('mypage:my_mood')
            else:
                searched = ','.join(selected_tags)
                return redirect(f'{reverse("mypage:my_mood_cafe")}?searched={searched}')

    else:
        # GET 요청일 때 (검색된 분위기 태그로 필터링)
        searched_term = request.GET.get('searched', '')
        searched_codes = searched_term.split(',')
        
        # 선택한 분위기 태그 객체 리스트
        search_tags = []
        search_tag_codes = []

        for code in searched_codes:
            tag_obj = Tag.objects.filter(code=code).first()
            if tag_obj:
                search_tags.append(tag_obj)
                search_tag_codes.append(tag_obj.code)

        # 유저가 투표한 모든 Mood_tags 정보 가져오기
        voted = Mood_tags.objects.filter(user_id=user.id).prefetch_related('tags')

        # 분위기 태그 겹치는 개수 세기
        overlap_counter = Counter()

        for vote in voted:
            cafe_id = vote.cafe_id
            voted_codes = [tag.code for tag in vote.tags.all()]
            overlap_count = sum(1 for code in voted_codes if code in search_tag_codes)
            if overlap_count > 0:
                overlap_counter[cafe_id] = overlap_count

        # 겹치는 수 기준으로 카페 id 정렬
        sorted_cafe_ids = [cafe_id for cafe_id, _ in overlap_counter.most_common()]

        if not sorted_cafe_ids:
            cafe_list = []
        else:
            # Case-When으로 정렬된 순서 유지
            preserved_order = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(sorted_cafe_ids)])
            sorted_cafes = Cafe.objects.filter(id__in=sorted_cafe_ids).order_by(preserved_order)

            # 각 카페에 이미지 붙이기
            cafe_list = []
            for cafe in sorted_cafes:
                image = CafeImage.objects.filter(cafe_id=cafe.id).first()
                cafe_list.append((cafe, image))

        context = {
            'cafe_list': cafe_list,
            'search_tags': search_tags
        }
        return render(request, 'mypage_moodselectlist.html', context)
