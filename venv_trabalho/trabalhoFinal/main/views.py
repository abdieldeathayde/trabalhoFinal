from django.shortcuts import render
from .models import Roupa

# Create your views here.

def list_page(request):
    obj=Roupa.objects.all()
    
    return render (request, 'list.html', {'obj':obj})
