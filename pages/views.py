from django.shortcuts import render, redirect
from .models import *
from books.models import Book
from articles.models import Article
import random


from django.contrib.auth.decorators import login_required

# Homepage
def home_view(request, *args, **kwargs):
	all_books_by_populartity = list(Book.objects.all().order_by('-popularity'))
	popular_books = lambda b: all_books_by_populartity[:3] if b > 3 else all_books_by_populartity
	all_articles_by_date = list(Article.objects.all().order_by('-date_created'))
	latest_article = all_articles_by_date[0]
	context = {
		'popular_books': popular_books(len(all_books_by_populartity)),
		'latest_article':latest_article,
	}
	return render(request, "home.html", context)


# Page with a list of organizations to support Ukraine
def support_view(request, *args, **kwargs):
	return render(request, "support.html", {})

# Random fact about Ukraine
def fact_view(request, *args, **kwargs):
	facts = list(Fact.objects.all())
	if len(facts) > 0:
		random_fact = random.choice(facts)
		return render(request, "random-fact.html", {"fact": random_fact, })
	else:
		return render(request, "random-fact.html", {})










