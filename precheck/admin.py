from django.contrib import admin
from django.contrib.auth.models import User
from .models import Checkpost,CheckImage
from django.utils.html import format_html


class CheckpostAdmin(admin.ModelAdmin):
    list_display = ('get_username','content', 'verified_check__user_type','get_checkimage' )  # 리스트에서 보여줄 필드 추가
    list_filter = ('verified_check__user_type',)  # 모델의 필터링
    search_fields = ('get_username',)  # 기본적인 검색 필드 설정
    
    def get_username(self, obj):
        return obj.user.username  # Checkpost 모델의 user 필드에서 username을 가져옴
    get_username.short_description = 'Username'
    
    def get_checkimage(self, obj):
        checkimage = obj.checkimage_set.first()  # CheckImage에서 첫 번째 이미지 가져오기
        if checkimage and checkimage.checkimage:
            return format_html('<img src="{}" style="width: 80px; height: 80px;" />', checkimage.checkimage.url)
        return "No Image"
    get_checkimage.short_description = "Check Image"


admin.site.register(Checkpost, CheckpostAdmin)
