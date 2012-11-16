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
    class Meta:
        model = Work
    
    
