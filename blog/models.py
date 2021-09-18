
from django.db import models
from django.contrib.auth.models import User
from django.urls.base import reverse
from django.utils import timezone
from django.utils.text import slugify
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    image=models.ImageField(upload_to = 'post/')
    discription = models.TextField(max_length=50000)
    user = models.ForeignKey(User, related_name ="autho", on_delete = models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now,)
    tags = TaggableManager()
    category = models.ForeignKey("Category", related_name="post_category", on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
       if not self.slug:
           self.slug= slugify(self.title)
       super(Post, self).save(*args, **kwargs) # Call the real save() method

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title





class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name