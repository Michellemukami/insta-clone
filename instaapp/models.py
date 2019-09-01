from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model): 
    profile_image = models.ImageField(upload_to = 'profile/', blank=True)
    username = models.CharField(max_length =60)
    gender = models.CharField(max_length =60)
    bio = HTMLField()
    user_id = models.IntegerField(default=0)
class Image(models.Model):
    image_name = models.CharField(max_length =60)
    image_caption = HTMLField()
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    like = models.IntegerField(null=True)
    insta_image = models.ImageField(upload_to = 'pixels/', blank=True)
    
    def __str__(self):
        return self.image_name
    def save_Image(self):
        self.save()

    def delete_Image(self):
        self.delete()
   
    def update_Caption(self):
        self.update()
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
