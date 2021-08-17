from django.db import models
from django.urls import reverse
import datetime

# Create your models here.

class Roupa(models.Model):
    roupa = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    
    class Meta:
        verbose_name = 'Roupa'
        verbose_name_plural = 'Roupas'
        
    def get_absolute_url (self):
        return reverse('trabalhoFinal:roupas_detail', args = [self.slug])
    
    def __str__(self):
        return self.slug
    