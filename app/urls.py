
from django.urls import path , include
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('envio/', views.envio , name='envio'),
    path('seguimiento/', views.seguimiento , name='seguimiento'),
]