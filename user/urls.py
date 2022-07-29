from django.urls import path
from .views import UserCreate, UserDetail

app_name = 'user'

urlpatterns = [
    path('', UserCreate.as_view(), name='createuser'),
    path('edit/', UserDetail.as_view(), name='edituser')
]