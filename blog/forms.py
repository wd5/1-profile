# -*- coding: utf-8 -*-
from django import forms

from models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['created',]

class CommentForm(forms.ModelForm):
    captcha = forms.CharField(label=u'Код с картинки',max_length=6)
    
    class Meta:
        model = Comment
        exclude = ['created', 'post']

