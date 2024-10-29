#!/usr/bin/python3

from django.contrib import admin

from .models import Chat, ChatMessage

#register the Chat and ChatMessage model to make it accessible in the django admin interface
admin.site.register(Chat)
admin.site.register(ChatMessage)
