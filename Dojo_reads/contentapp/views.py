from django.shortcuts import render, redirect, HttpResponse
from ReadApp.models import User
from .models import Author, Book, Review
from django.contrib import messages
# import bcrypt

def index(request):
    if not 'user_id' in request.session:
        
        return redirect('/')
    
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'our_user': user,
        'reviews' : Review.objects.all().reverse()[:3],
        'books': Book.objects.all()
    }
    return render(request, 'welcome.html', context)

def add_page(request):
    if not 'user_id' in request.session:
        return redirect('/')
    authors = Author.objects.all()
    context = {
                'authors': authors
    }

    return render(request, 'add_book.html', context)

def add_review(post, book, user_id):
    Review.objects.create(
                        words = post['review'],
                        stars = post['stars'],
                        book = book,
                        user = User.objects.get(id=user_id)
    )



def add_book(request):
    
    # book validator
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/books/add')
    
    if request.POST['add_author'] == "":
        author = Author.objects.create(
                            name = request.POST['author']
        )
    else:
        author = Author.objects.create(
                            name = request.POST['add_author']
        )
    
    book = Book.objects.create(title = request.POST['title'],
                        author = author  
                        )
    add_review(request.POST, book, request.session['user_id'])
    return redirect('/books/' + str(book.id))


def book_info(request, book_id):
    if not 'user_id' in request.session:
        return redirect('/')

    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'book_info.html', context)

def review(request, book_id):
    # errors = Review.objects.review_validator(request.POST)
    # if len(errors) > 0:
    #     for key, value in errors.items():
    #         messages.error(request, value)

    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['user_id'])
    Review.objects.create(
                        words = request.POST['review'],
                        stars = request.POST['stars'],
                        book = book,
                        user = user
    )
    return redirect('/books/' + str(book_id))

def delete_review(request, review_id, book_id):
    review = Review.objects.get(id=review_id)
    review.delete()


    return redirect('/books/' +str(book_id))

def user_info_page(request, users_id):
    user = User.objects.get(id=users_id)
    reviews = Review.objects.filter(user_id=users_id)
    our_user = User.objects.get(id=request.session['user_id'])
    print(our_user.name)
    context = {
            'user': user,
            'reviews': reviews,
            'our-user': our_user
            }
    return render(request, 'user_info.html', context)
