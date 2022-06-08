from django.urls import path

from . import views

urlpatterns = [
    path('hauntedmansiontwo', views.hauntedmansiontwo, name='hauntedmansiontwo'),
]