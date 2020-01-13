from django.urls import path
from . import views

urlpatterns = [
    path('f_add', views.f_add, name='feedback_add'),
    path('', views.index, name='feedbacks_view'),
]
