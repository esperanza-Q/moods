from django.urls import path
from .views import precheck, precheck_A, precheck_B, test, precheck_delete

app_name = 'precheck'

urlpatterns = [
    path('<int:user_id>', precheck, name='precheck'),
    path('<int:user_id>/<int:checkpost_id>/', precheck_A, name='precheck_A'),
    path('<int:user_id>/precheck_B/', precheck_B, name='precheck_B'),
    path('<int:user_id>/precheck_delete/<int:checkpost_id>', precheck_delete, name='precheck_delete'),
    path('test', test, name='test'),

]