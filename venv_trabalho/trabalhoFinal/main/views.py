from django.shortcuts import render
from .models import Ingrediente

# Create your views here.

def list_page(request):
    obj=Ingrediente.objects.all()
    
    return render (request, 'list.html', {'obj':obj})
