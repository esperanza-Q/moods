from django.urls import path
from .views import select_before, select_searched, select_detail, review, select_tag, reselect_tag

app_name = 'cafe_select'

urlpatterns = [
    path('select_before/', select_before, name='select_before'),
    path('select_searched/', select_searched, name='select_searched'),
    path('select_detail/<int:cafe_id>', select_detail, name='select_detail'),
    path('select_detail/<int:cafe_id>/review', review, name='review'),
    path('select_detail/<int:cafe_id>/select_tag', select_tag, name='select_tag'),
    path('select_detail/<int:cafe_id>/reselect_tag', reselect_tag, name='reselect_tag'),
]