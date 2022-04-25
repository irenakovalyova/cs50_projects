from django.db import models
from django.contrib.auth.models import User
from books.models import Book
from djrichtextfield.models import RichTextField

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    bio = RichTextField(blank=False, null=False, )
    avatar = models.ImageField(blank=True, null=True, upload_to='img/profile-photos/', )
