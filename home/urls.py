from django.urls import path
from .views import home, prehome

app_name = 'home'

urlpatterns = [
    path('prehome/', prehome, name='prehome'),
    path('home/<int:user_id>', home, name='home'),
]