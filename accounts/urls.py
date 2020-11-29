from django.urls import path

from . import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('register.html', views.register, name='register'),
    path('login.html', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('destinations.html', views.destinations, name='destinations'),
]
