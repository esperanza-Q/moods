from django.contrib import admin
from django.utils.html import format_html
from .models import Cafe, CafeImage

class CafeInline(admin.StackedInline):
    model = CafeImage  # Profile을 User에 연결
    fields = ('cafeimage',)  # user_type 필드만 편집할 수 있게 설정
    can_delete = False  # Profile을 삭제할 수 없게 설정
    verbose_name_plural = 'Cafe Images'

class CafeAdmin(admin.ModelAdmin):
    list_display = ('cafename','cafelocations', 'cafeinfo', 'get_cafeimage')  # 리스트에서 보여줄 필드 추가
    # list_filter = ('verified_check__user_type',)  # 모델의 필터링
    search_fields = ('cafename', 'cafelocations')  # 기본적인 검색 필드 설정
    
    inlines = [CafeInline]
    
    def get_cafeimage(self, obj):
        cafe_image = obj.cafeimage_set.first()  # Cafe와 관련된 첫 번째 CafeImage 객체를 가져옴
        if cafe_image:
            return format_html('<img src="{}" width="100" height="100" />', cafe_image.cafeimage.url)  # cafeimage 필드 반환
        return None
    get_cafeimage.short_description = 'Cafe Image'

admin.site.register(Cafe, CafeAdmin)
