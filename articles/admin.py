from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    readonly_fields=('user', 'article', 'comment_text')
    list_display = ['user', 'comment_text', 'date_created']

    def has_add_permission(self, request, obj=None):
        return False

class ArticleAdmin(admin.ModelAdmin):
    # a list of displayed columns name.
    list_display = ['title', 'author', 'date_created']
    list_filter = ['author', 'category']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
