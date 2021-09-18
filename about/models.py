from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class About(models.Model):
    image=models.ImageField(upload_to='about/')
    what_we_do = models.TextField(max_length=1000)
    our_mission = models.TextField(max_length=1000)
    our_goals = models.TextField(max_length=1000)
    def __str__(self):
        return str(self.id)

class Faq(models.Model):
    title = models.CharField(max_length=200)
    discription=models.TextField(max_length=1000)

    def __str__(self):
        return self.title