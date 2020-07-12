from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    #include the built-in auth urls
    path('accounts/', include('django.contrib.auth.urls')),
    #New urls for sign up
    path('accounts/signup', views.signup, name='signup'),
]

