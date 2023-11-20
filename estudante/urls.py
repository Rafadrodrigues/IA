from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='Index'),
    path('adicionar/', views.adicionar,name='Adicionar')
]
