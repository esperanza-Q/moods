from django.contrib import admin
from django.contrib.auth.models import User
from .models import Checkpost



class CheckpostAdmin(admin.ModelAdmin):
    list_display = ('get_username','content', 'verified_check__user_type')  # 리스트에서 보여줄 필드 추가
    list_filter = ('verified_check__user_type',)  # 모델의 필터링
    search_fields = ('get_username',)  # 기본적인 검색 필드 설정
    
    def get_username(self, obj):
        return obj.user.username  # Checkpost 모델의 user 필드에서 username을 가져옴
    get_username.short_description = 'Username'

admin.site.register(Checkpost, CheckpostAdmin)
