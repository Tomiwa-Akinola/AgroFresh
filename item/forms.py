#!/usr/bin/python3

from django import forms

from .models import Item

#css class for styling imput fields
INPUT_CLASSES =  'w-full py-4 px-6 rounded-xl border'

#form for creating a new item
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)

        widgets = {
                'category': forms.Select(attrs={
                    'class': INPUT_CLASSES
                    }),
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                    }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                    }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                    }),
                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES
                    })
                }

#form for editing an existing item
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
                'name': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                    }),
                'description': forms.Textarea(attrs={
                    'class': INPUT_CLASSES
                    }),
                'price': forms.TextInput(attrs={
                    'class': INPUT_CLASSES
                    }),
                'image': forms.FileInput(attrs={
                    'class': INPUT_CLASSES
                    })
                }
