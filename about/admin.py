from django.contrib import admin

# Register your models here.
from .models import About , Faq
admin.site.register(About)
admin.site.register(Faq)