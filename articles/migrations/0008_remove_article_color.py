# Generated by Django 4.0.3 on 2022-04-16 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='color',
        ),
    ]
