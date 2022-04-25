# Generated by Django 4.0.3 on 2022-03-24 22:31

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0012_alter_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='1', editable=False, populate_from='title'),
        ),
    ]
