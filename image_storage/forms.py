# -*- coding: utf-8 -*-
from django import forms

class AddImg(forms.Form):
    app_id = forms.IntegerField(required=True)
    file_var = forms.FileField(required=True)
    tag = forms.CharField(max_length=64,required=False)
    
