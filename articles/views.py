from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from books.models import Category, Book
import random
from .forms import CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
)

# Generic view for the article list

class ArticleListView(ListView):
    template_name = 'articles.html'
    paginate_by = 5


    def get_category(self):
        return self.request.GET.get('category', default=None)

    def get_queryset(self):
        queryset = Article.objects.all()
        category_name = self.get_category()
        if category_name: # If the page is requested with a category filter
            category = Category.objects.filter(name=category_name)
            if category:
                queryset = Article.objects.all().filter(category=category[0].id)
            else:
                return None # Show empty list if there is no such category
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        all_categories = list(Category.objects.all())
        context['categories'] = random.sample(all_categories, 7) # Only 7 slots for categories on the page
        context['category'] = self.get_category()
        return context


# Generic view for a single article with comment option

class ArticleDetailView(UpdateView):
    model = Article
    template_name = 'article-details.html'
    form_class = CommentForm


    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Article, slug=slug_)

    def get_success_url(self):
        object = self.get_object()
        return object.get_absolute_url()

    def get_recommended_book(self):     # Get random book from the same category
        object = self.get_object()
        if object.related_book:
            recommended_book = object.related_book
        else:
            similar_books = list(Book.objects.filter(category=object.category))
            recommended_book = random.choice(similar_books)
        return recommended_book

    def get_similar_articles(self):     # Get 3 random articles from the same category
        object = self.get_object()
        similar = set(Article.objects.filter(category=object.category).exclude(id=object.id))
        n = lambda l: 3 if l > 2 else l
        similar_articles = random.sample(similar, n(len(similar)))
        return similar_articles

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        intaial_data = {            # Prefill hidden form fields with initial data
        'user': self.request.user.id,
        'article': self.object.id
        }
        context['form'] = CommentForm(self.request.POST or None, initial=intaial_data)
        context['recommended_book'] = self.get_recommended_book()
        context['similar_articles'] = self.get_similar_articles()
        return context

    def post(self, request, *args, **kwargs): # Post a comment
        self.object = self.get_object()
        context = self.get_context_data()
        form = context['form']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(ArticleDetailView, self).form_valid(form)






