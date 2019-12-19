from django.urls import path
from . import views

urlpatterns = [
    path('mp_add', views.page_add, name='page_add'),
    path('t_add', views.ticket_add, name='ticket_add'),
    path('<int:id>', views.ticket_view, name='ticket'),
    path('', views.m_start, name='m_start'),
]
