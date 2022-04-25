from django.shortcuts import render, redirect
from .models import Book, Category
from articles.models import Article
from django.db.models import F

# Create your views here.

# Book list
def books_list_view(request, *args, **kwargs):
    books = list(Book.objects.all())
    category_name = request.GET.get('category', default=None)

    if category_name:               # Filter books if a category requested
        category = list(Category.objects.filter(name=category_name))
        if category:
            books = set(Book.objects.filter(category=category[0]))
            return render(request, "books.html", {"books": books, "category": category_name,})
        else:
            return render(request, "books.html", {"books": set(), "category": category_name,})

    return render(request, "books.html", {"books": books,})


# Detailed book page view
def book_details_view(request, slug, *args, **kwargs):
    book = Book.objects.get(slug=slug)
    Book.objects.filter(id=book.id).update(popularity=F('popularity') + 1)

    recommended = book.get_recommended_books()
    reviews = set(Article.objects.filter(related_book=book.id).filter(category=Category.objects.get(name='Book reviews')))
    is_favourite = book.is_favourite(request.user.id)
    context = {'book': book,
               'recommended': recommended,
               'reviews': reviews,
               'is_favourite': is_favourite,
               }
    return render(request, "book-details.html", context)


