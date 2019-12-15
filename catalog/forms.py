from django import forms
from django.forms import ModelForm
from catalog.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
