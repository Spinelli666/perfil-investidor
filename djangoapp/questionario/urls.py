from django.urls import path
from . import views

app_name = 'questionario'

urlpatterns = [
    path('', views.home, name='home'),
    path('questionario/', views.questionario, name='questionario'),
    path('resultado/', views.resultado, name='resultado'),
]
