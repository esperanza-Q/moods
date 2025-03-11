from django.urls import path
from .views import mypage, profile_update
app_name = 'mypage'

urlpatterns = [
    path('<int:user_id>/', mypage, name='mypage'),
    path('<int:user_id>/update/', profile_update, name='profile_update'),
]