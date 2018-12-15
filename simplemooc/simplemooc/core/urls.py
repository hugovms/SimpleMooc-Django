from django.contrib import admin
from django.urls import path
from django.urls import include
from simplemooc.core import views
admin.autodiscover()

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contact, name='contact'),
    path('cursos/', views.cursos, name='cursos'),
]