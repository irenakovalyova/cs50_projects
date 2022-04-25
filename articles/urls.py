from django.urls import path
from .views import (
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    ]
