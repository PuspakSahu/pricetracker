from django.urls import path
from . import views

urlpatterns = [
    path('', views.details ,name='details'),
    path('notice1/', views.notice1 ,name='notice1')
] 
