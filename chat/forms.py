#!/usr/bin/python3

from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ('content',)  #specifying field to include in the form
        widgets = {
                'content': forms.Textarea(attrs={   #customizing widget for the 'content' field
                    'class': 'w-full py-4 px-6 rounded-xl border'   #css classes for styling
                    })
                }
