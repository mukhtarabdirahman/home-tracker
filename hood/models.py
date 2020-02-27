from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Neighbourhood(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=30)
    location = models.CharField(max_length = 60)

    @classmethod
    def search_by_location(cls,search_term):
        location = cls.objects.filter(location__icontains=search_term)
        return location
    def save_neighbourhood(self):
        self.save()
    def delete_neighbourhood(self):
        self.delete()
