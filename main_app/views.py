from django.shortcuts import render, redirect, get_object_or_404
from . import views, forms
from .models import Book
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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


def book_create(request):
    if request.method == 'POST':
        form = forms.CreateBook(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/books/')
    else:
        form = forms.CreateBook()
    return render(request, 'books/book_create.html', {'form': form})

class BookUpdate(UpdateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'illustrated', 'age', 'bookImage', 'bookPdf']
    success_url = '/books/'


class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

def home(request):
    return render(request, 'home.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', { 'books': books })

def books_detail(request, pk):
    book = Book.objects.get(id=pk)
    liked = False
    if book.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'book': book,
        'liked': liked,
        'total_likes': book.total_likes(),
    }
    
    return render(request, 'books/detail.html', context)

def LikeView(request, pk):
    book = get_object_or_404(Book, id=request.POST.get('book_id'))
    liked = False
    if book.likes.filter(id=request.user.id).exists():
        book.likes.remove(request.user)
        liked = False
    else:
        book.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse(books_detail, args=[str(pk)]))

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
