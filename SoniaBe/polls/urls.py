from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('',views.index, name = 'index'),
    path('<str:layoutName>/layout/',views.layout, name = 'layout'),
]