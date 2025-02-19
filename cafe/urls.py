from django.urls import path
from .views import cafeadd

app_name = 'cafe'

urlpatterns = [
    path('cafeadd/', cafeadd, name='cafeadd'),

]