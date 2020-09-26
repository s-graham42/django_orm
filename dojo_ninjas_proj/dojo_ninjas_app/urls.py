from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_a_dojo', views.add_a_dojo),
    path('add_a_ninja', views.add_a_ninja),
    path('delete_a_dojo', views.delete_a_dojo),
]
