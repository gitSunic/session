from django.urls import path
from . import views

urlpatterns = [
    path('', views.p_start, name='p_start'),
]
