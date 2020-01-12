from django.urls import path
from . import views

urlpatterns = [
    path('min', views.min, name='minimum'),
    path('mp_add', views.page_add, name='page_add'),
    path('t_add', views.ticket_add, name='ticket_add'),
    path('<int:id>', views.ticket_view, name='ticket'),
    path('', views.p_start, name='p_start'),
]
