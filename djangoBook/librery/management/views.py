from django.shortcuts import render,get_object_or_404,redirect
from .models import Book, User, Rental
from .forms import BookForm, RentalForm

def book(request):
    if request.method == 'POST':
        form = Book(request.POST)
        form.save()
    bk = Book.objects.all()
    form = Book()
    contex = {
        'bk' : bk,
        'form': form
    }
    return render(request,'base.html', contex)

def search(request):
    books = Book.objects.all()
    genres = set()
    for book in books:
        genres.add(book.genre)
        
    contex = {
        'genres': genres
    }
    return render(request,'search.html', contex)


def genre(request, genre):
  book_list = Book.objects.filter(genre=genre)
  h1 = set()
  for h1_genre in book_list:
      h1.add(h1_genre.genre)
  return render(request, 'genre.html', context={'books': book_list, 'h1':h1})


def users(request):
    users = User.objects.all()
    return render(request,'users.html', context={"users": users})

def books_in_users(request, username):
    user = User.objects.get(username=username)
    book_list = Rental.objects.filter(user=user)
    h1 = set()
    for h1_user in book_list:
        h1.add(h1_user.user)
    return render(request, 'books_in_users.html', context={'book_list':book_list,'h1':h1})


def free_list(request):
    book_list_free = Book.objects.filter(is_available=True)
    return render(request,'free_list.html',context={'book_list_free':book_list_free})



def edit_book(request,id):
    book = get_object_or_404(Book,id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect ('book')
    return render (request,'edit_book.html', context={'form': BookForm(instance=book), 'id':id})


def delete_book(request,id):
    if request.method == 'POST':
        form = Book.objects.get(pk=id)
        form.delete()
        return redirect ('book')
    book = Book.objects.get(pk=id)
    return render (request,'delete_book.html', context={'book': book})


def add_book(request):#Непонятно почему при создании книги пункт "is_available" - 'False" , хотя по умолчанию 'True"
    if request.method == 'POST':
        form = BookForm(request.POST)
        form.save()
        return redirect('book')
    form = BookForm(request.POST)
    data = {
        'form': form
    }
    return render(request,'add_book.html', data)


def rent(request):
    if request.method == 'POST':
        form = RentalForm(request.POST)
        form.save()
        redirect('book')
    form = RentalForm(request.POST)
    return render(request,'rent.html',context={'form':form})