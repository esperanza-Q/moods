from django.urls import path
from .views import precheck, precheck_A, precheck_B, test, precheck_delete

app_name = 'precheck'

urlpatterns = [
    path('', precheck, name='precheck'),
    path('precheck_A/', precheck_A, name='precheck_A'),
    path('precheck_B/', precheck_B, name='precheck_B'),
    path('precheck_delete/<int:checkpost_id>', precheck_delete, name='precheck_delete'),
    path('test', test, name='test'),

]