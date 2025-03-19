from django.urls import path
from .views import home, prehome, firstpage

app_name = 'home'

urlpatterns = [
    path('', firstpage, name='firstpage'),
    path('prehome/', prehome, name='prehome'),
    path('home/<int:user_id>', home, name='home'),
]