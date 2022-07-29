from django.urls import path
from . import views

urlpatterns = [
    path('', views.open_position),
    path('close/<int:id>', views.close_position)
]
