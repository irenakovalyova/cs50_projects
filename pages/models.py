from django.db import models


# Create your models here.

class Fact(models.Model):
    summary = models.TextField(blank=False, null=False, )
    details = models.TextField(blank=False, null=False, )

    def __str__(self):
        return self.summary
