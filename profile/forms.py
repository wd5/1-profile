# -*- coding: utf-8 -*-
from django import forms

from models import Profile, Work

class EditProfile(forms.ModelForm):
    avatar = forms.FileField(required=False)
    
    class Meta:
        model = Profile
        exclude = ['active','avatar']
        #fields = []

class FormWork(forms.ModelForm):
    begin = forms.DateField(widget=forms.TextInput(attrs={'class': 'date '}))
    end = forms.DateField(widget=forms.TextInput(attrs={'class': 'date '}),
                          required=False)
    
    class Meta:
        model = Work
    
    
