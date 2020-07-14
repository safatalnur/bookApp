from django.urls import path, include
from . import views
from .views import LikeView

urlpatterns = [
    path('', views.home, name='home'),
    #View for all books
    path('books/', views.books_index, name='index'),
    #View for a book in details
    path('books/<int:pk>/', views.books_detail, name='detail'),
    # View for like individual book
    path('like/<int:pk>', LikeView, name='like_book'),   
    # View to create a new book
    path('books/create/', views.book_create, name='create'),
    # View to edit a book
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    # To delete a book
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    #include the built-in auth urls
    path('accounts/', include('django.contrib.auth.urls')),
    #New urls for sign up
    path('accounts/signup', views.signup, name='signup'),
]

