from django.contrib import admin
from .models import Review
# Register your models here.

# admin.site.unregister(Review)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('cafe', 'user', 'review_image', 'review_content')  # 리스트에서 보여줄 필드 추가
    list_filter = ('cafe','user')  # Profile 모델의 `user_type`으로 필터링
    search_fields = ('cafe', 'user', 'review_content')  # 기본적인 검색 필드 설정

admin.site.register(Review, ReviewAdmin)