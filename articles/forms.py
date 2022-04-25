from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'user',
            'article',
            'comment_text',
        ]

        labels = {              # Remove field labels
            "comment_text": ""
        }

        widgets = {                     # Set article and user fields as hidden from page
            'article': forms.HiddenInput(),
            'user': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['comment_text'].widget.attrs['class'] = 'article-page-textarea textarea' # Set custom CSS style
        self.fields['comment_text'].widget.attrs['placeholder'] = 'Type your comment' # Set field placeholder

