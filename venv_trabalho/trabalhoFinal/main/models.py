from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Ingrediente(models.Model):
    ingrediente1 = models.CharField(max_length=100)
    ingrediente2 = models.CharField(max_length=100)
    ingrediente3 = models.CharField(max_length=100)
    ingrediente4 = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        
    def get_absolute_url (self):
        return reverse('main:ingrediente_detail', args = [self.slug])
    
    def __str__(self):
        return self.nome
    