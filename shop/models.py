from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='categories')

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
    def __str__(self):
        return '{}'.format(self.name)

    
class products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=1000,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    class Meta:
        ordering=('name',)
        verbose_name='products'
        verbose_name_plural='Products'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('pr',args=[self.slug])

    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

    