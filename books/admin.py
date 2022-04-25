from django.contrib import admin
from .models import Book
from .models import Category

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields=('popularity',)
    list_display = ['title', 'author',]

admin.site.register(Book, BookAdmin)
admin.site.register(Category)
