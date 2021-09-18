from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, DateTimeField, IntegerField
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='properity')
    price = models.IntegerField(default=0)
    place = models.ForeignKey("Place",related_name="property_place",on_delete=models.CASCADE)
    category = models.ForeignKey("Category",related_name="property_category",on_delete=models.CASCADE)
    slug=models.SlugField(null=True ,blank=True)

    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug= slugify(f'{self.name}')
       super(Property, self).save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse("property:property_detial", kwargs={"slug": self.slug})
    
    def __str__(self):
        return self.name
    

class Images(models.Model):
    property = models.ForeignKey(Property,related_name="property_images",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyimages')
    def __str__(self):
        return str(self.property)

class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='places/')
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class PropertyReview(models.Model):
    user = models.ForeignKey(User,related_name="author",on_delete=models.CASCADE)
    property = models.ForeignKey(Property,related_name="property_review",on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)
    feedback = models.TextField(max_length=2000)
    def __str__(self):
        return str(self.property)
count=(
    (1,1),
(2,2),
(3,3),
(4,4),
(5,5))
class PropertyBook(models.Model):
    user = models.ForeignKey(User,related_name="book_owner",on_delete=models.CASCADE)
    property = models.ForeignKey(Property,related_name="property_book",on_delete=models.CASCADE)
    date_from = models.DateTimeField(default=timezone.now)
    date_to = models.DateTimeField(default=timezone.now)
    guest=models.TextField(choices=count)
    childern=models.TextField(choices=count)
    def __str__(self):
        return str(self.property)
        