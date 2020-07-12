from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    #View for all books
    path('books/', views.books_index, name='index'),
    #View for a book in details
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    # View to create a new book
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    #include the built-in auth urls
    path('accounts/', include('django.contrib.auth.urls')),
    #New urls for sign up
    path('accounts/signup', views.signup, name='signup'),
]

