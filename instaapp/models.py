from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField



class Image(models.Model):
    image_name = models.CharField(max_length =60)
    image_caption = HTMLField()
    profile = models.ForeignKey(Profile)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.IntegerField(null= none)
    insta_image = models.ImageField(upload_to = 'pixels/', blank=True)
    check(like=1 or like=-1)
    def __str__(self):
        return self.name
    def save_Image(selpost = models.TextField()f):
        self.save()

    def delete_Image(self):
        self.delete()
   
    def update_Caption(self):
        self.update()

class Profile(models.Model): 
    profile_image = models.ImageField(upload_to = 'profile/', blank=True)
    bio = HTMLField()