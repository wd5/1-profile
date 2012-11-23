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
    begin = MyDateField()
    end = MyDateField(required=False)
    
    class Meta:
        model = Work
    
    
