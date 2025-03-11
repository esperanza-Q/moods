from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Profile 모델을 User 모델에 포함시키기 위한 Inline 모델
class UserInline(admin.StackedInline):
    model = Profile  # Profile을 User에 연결
    fields = ('user_type',)  # user_type 필드만 편집할 수 있게 설정
    can_delete = False  # Profile을 삭제할 수 없게 설정
    verbose_name_plural = 'Profile'

# 기존 UserAdmin 해제
admin.site.unregister(User)

# UserAdmin 수정
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_user_type')  # 리스트에서 보여줄 필드 추가
    list_filter = ('profile__user_type',)  # Profile 모델의 `user_type`으로 필터링
    search_fields = ('username', 'email')  # 기본적인 검색 필드 설정

    # ProfileInline을 추가하여 `Profile` 정보를 `User` Admin에 포함시킴
    inlines = [UserInline]

    # `Profile`에서 `user_type`을 가져오는 메서드
    def get_user_type(self, obj):
        return obj.profile.user_type if obj.profile else None
    get_user_type.short_description = 'User Type'

    # 수정 액션 추가
    def make_verified(self, request, queryset):
        for user in queryset:
            user.profile.user_type = 'verified'  # Profile의 user_type 수정
            user.profile.save()  # 변경사항 저장
    make_verified.short_description = 'Set selected users as Verified'

    def make_guest(self, request, queryset):
        for user in queryset:
            user.profile.user_type = 'guest'  # Profile의 user_type 수정
            user.profile.save()  # 변경사항 저장
    make_guest.short_description = 'Set selected users as Guest'

    # 액션 등록
    actions = [make_verified, make_guest]
