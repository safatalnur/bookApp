from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    #include the built-in auth urls
    path('accounts/', include('django.contrib.auth.urls')),
    #New urls for sign up
    path('accounts/signup', views.signup, name='signup'),
]

