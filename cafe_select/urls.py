from django.urls import path
from .views import select_before, select_searched, select_detail, review

app_name = 'cafe_select'

urlpatterns = [
    path('<int:user_id>/select_before/', select_before, name='select_before'),
    path('<int:user_id>/select_searched/', select_searched, name='select_searched'),
    path('<int:user_id>/select_detail/<int:cafe_id>', select_detail, name='select_detail'),
    path('<int:user_id>/select_detail/<int:cafe_id>/review', review, name='review'),
]