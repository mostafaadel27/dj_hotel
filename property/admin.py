from django.contrib import admin

# Register your models here.
from .models import Property , Images , Place , Category , PropertyReview , PropertyBook
admin.site.register(Property)
admin.site.register(Images)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyReview)
admin.site.register(PropertyBook)