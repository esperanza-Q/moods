from django.urls import path
from .views import mypage, profile_update
app_name = 'mypage'

urlpatterns = [
    path('', mypage, name='mypage'),
    path('update/', profile_update, name='profile_update'),
]