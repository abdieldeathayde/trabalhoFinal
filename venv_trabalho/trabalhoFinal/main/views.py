from django.shortcuts import render
from .models import Roupa

# Create your views here.

def EscolheRoupa(request):
    obj=Roupa.objects.all()
    
    return render (request, 'trabalhoFinal/list_roupas.html', {'obj':obj})
