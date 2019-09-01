from django.contrib import admin
from .models import Image,Profile
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
   

admin.site.register(Image,ImageAdmin)
admin.site.register(Profile)
