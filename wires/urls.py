from django.urls import path
from . import views

urlpatterns = [
    path('', views.wire_transfer)
]
