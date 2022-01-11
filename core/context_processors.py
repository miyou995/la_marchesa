from django.shortcuts import render , get_object_or_404
from .models import Category

def trees(request):
    categories = Category.objects.filter(level=0, actif=True)
    context = {
        'categories' : categories,
        }
    return context
    

