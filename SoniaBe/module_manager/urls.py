from django.urls import path
from . import views


app_name = 'module_manager'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<str:layoutName>/layout/',views.layout, name = 'layout'),
]