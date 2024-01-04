from django.db import models
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    name=models.CharField( max_length=250)
    slug=models.SlugField(max_length=250)
    description=models.CharField( max_length=500)

    class meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.name
    def get_url(self):
        return reverse('category_view' , args=[self.slug])

    

class Product(models.Model):

    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=500)
    descr=models.TextField(blank=True)
    price=models.DecimalField( max_digits=5, decimal_places=2)
    category=models.ForeignKey('Category', on_delete=models.CASCADE)
    image=models.ImageField( upload_to='product',  blank=True)
    available=models.BooleanField(default=True)
    stock=models.IntegerField()
    
        
    
    class Meta:
        ordering=('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self):
        return self.name

