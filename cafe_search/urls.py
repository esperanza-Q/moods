from django.urls import path
from .views import search_before, search_after, search_detail

app_name = 'cafe_search'

urlpatterns = [
    path('search_before/', search_before, name='search_before'),
    path('search_after/', search_after, name='search_after'),
    path('search_detail/<int:cafe_id>', search_detail, name='search_detail'),
]