from django.shortcuts import render, redirect
from . import views
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#Creating temporary data for all books page
# class Book:
#     def __init__(self, title, author, illustrated, age):
#         self.title = title
#         self.author = author
#         self.illustrated = illustrated
#         self.age = age

# books = [
#     Book('Hide and Seek', 'T. Albert', 'maaillustrations.com', 'Age: 2-6'),
#     Book('Ginger The Giraffe', 'T. Albert', 'maaillustrations.com', 'Age: 2-6'),
#     Book('I Found a Frog', 'T. Albert', 'maaillustrations.com', 'Age: 2-6'),
# ]

# Create your views here.

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def home(request):
    return render(request, 'home.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', { 'book': book })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('books')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
