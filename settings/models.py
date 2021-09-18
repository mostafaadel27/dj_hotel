from django.db import models

# Create your models here.
class Settings(models.Model):
    site_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='settings/')
    addrees = models.TextField(max_length=1000)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    description = models.TextField(max_length=1000)
    facebook = models.URLField(max_length=300)
    twitter = models.URLField(max_length=300)
    instgram = models.URLField(max_length=300)

    def __str__(self):
        return self.site_name
    

