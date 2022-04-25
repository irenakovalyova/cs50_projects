from django.db import models
from books.models import Category, Book
from autoslug import AutoSlugField
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=250, )
    summary = models.TextField(blank=False, null=False, )
    image = models.ImageField(blank=False, null=False, upload_to='img/', )
    text = RichTextField(blank=False, null=False, )
    category = models.ForeignKey(Category, null=True, blank=True, default='', on_delete=models.SET_DEFAULT)
    featured = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title')
    related_book = models.ForeignKey(Book, null=True, blank=True, default='', on_delete=models.SET_DEFAULT)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"slug": self.slug})

    def get_comments(self):
        return Comment.objects.filter(article=self.id)


    author = models.ForeignKey(User, null=True, blank=True, default='', on_delete=models.SET_DEFAULT)



    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.ImageField(blank=False, null=False, upload_to='img/', )

class Comment(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, )
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE, )
    comment_text = models.TextField(blank=False, null=False, max_length=500,)
    date_created = models.DateField(auto_now_add=True, )

    def __str__(self):
        return self.comment_text

