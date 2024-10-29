from django.contrib import admin

from .models import Category, Item

#register the Category and Item models with the admin site
admin.site.register(Category)
admin.site.register(Item)
