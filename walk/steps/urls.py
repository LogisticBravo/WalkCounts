from django.urls import path
from .import views


urlpatterns = [
    path('', views.steps, name='steps'),
]
