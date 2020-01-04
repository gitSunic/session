from django.urls import path
from . import views

urlpatterns = [
    path('min', views.min, name='minimum'),
    path('', views.p_start, name='p_start'),
]
