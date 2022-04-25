from django.contrib import admin
from .models import *

# Register your models here.

class CommentModelAdmin(admin.ModelAdmin):
    actions = ['delete']

admin.site.register(Fact)

