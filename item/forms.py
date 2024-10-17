#!/usr/bin/python3

from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'desceiption', 'price', 'image',)
