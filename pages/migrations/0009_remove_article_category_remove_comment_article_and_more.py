# Generated by Django 4.0.3 on 2022-04-08 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_article_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
