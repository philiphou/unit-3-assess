from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.widget_create, name='create'),
    path('delete/<int:widgetid>/', views.widget_delete, name='delete'),
]