from django.db import models
from autoslug import AutoSlugField
from colorfield.fields import ColorField
import random
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    COLOR_PALETTE = [
        ('#696969', 'Architecture', ), #grey
        ('#0E61CB', 'General', ), #blue
        ('#5F9834', 'Literature', ), #green
        ('#FF8300', 'Cuisine', ), #orange
        ('#5A4FCF', 'Culture', ), #purple
        ('#FF4500', 'History', ), #red
        ('#FC3C80', 'Book reviews') #pink
    ]

    name = models.CharField(max_length=120, unique=True,)
    color = ColorField(choices=COLOR_PALETTE)

    def get_theme_color(self):
        theme_color_palette = {"Architecture": "#cbcbcb", #grey
        "General": "#B8E1F6", #blue
        "Literature": "#84c554", #green
        "Cuisine": "#ffa84d", #orange
        "Culture": "#928bdf", #purple
        "History": "#ff7e4d", #red
        "Book reviews": "#fd87b1" #pink
        }

        if self.name in theme_color_palette.keys():
            return theme_color_palette[self.name]
        else:
            return "#B8E1F6"



    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=120, )
    summary = models.CharField(max_length=120, )
    author = models.CharField(max_length=120, )
    description = models.TextField(blank=True, null=True, )
    price = models.DecimalField(default=0, decimal_places=2, max_digits=4)
    image = models.ImageField(blank=True, null=True, upload_to='img/books/', )
    category = models.ForeignKey(Category, null=True, blank=True, default='', on_delete=models.SET_DEFAULT)
    featured = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title')
    buy_url = models.URLField(max_length=200, blank=True, null=True, default='',)
    popularity = models.IntegerField(default=0)
    favourites = models.ManyToManyField(User, blank=True, default=None, related_name='favourites')
    quote = models.TextField(blank=True, null=True, default='')

    def __str__(self):
        return self.title


    def get_recommended_books(self):
        similar_books = set(Book.objects.filter(category=self.category).exclude(slug=self.slug))
        n = lambda l: 3 if l > 2 else l
        return random.sample(similar_books, n(len(similar_books)))

    def is_favourite(self, id):
        return self.favourites.filter(id=id).exists()

