from django.urls import path
from .views import mypage, profile_update, my_review, delete_myreview, my_mood, my_mood_cafe

app_name = 'mypage'

urlpatterns = [
    path('', mypage, name='mypage'),
    path('update/', profile_update, name='profile_update'),
    path('myreview/', my_review, name='my_review'),
    path('myreview/<int:cafe_id>/delete_myreview/', delete_myreview, name='delete_myreview'),
    path('mymood/', my_mood, name='my_mood'),
    path('mymoodcafe/', my_mood_cafe, name='my_mood_cafe'),
]