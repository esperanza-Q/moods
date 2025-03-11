from django.urls import path
from .views import cafeadd

app_name = 'cafe'

urlpatterns = [
    path('<int:user_id>/cafeadd', cafeadd, name='cafeadd'),

]