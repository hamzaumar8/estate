from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='sample.jpg', upload_to='profile_pics')
    department = models.CharField(max_length=200, null=True, blank=True)
    allow_access = models.BooleanField(default=True)

    def __str__(self):
        return self.user.email

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url


def profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        print('checK', instance.id)
        profile = Profile.objects.create(user=instance)

post_save.connect(profile_receiver, sender=User)

# USER REGISTRATION MODEL
class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    home = models.ForeignKey("Home", on_delete=models.SET_NULL, related_name='tenanthome', null=True, blank=True)
    name =  models.CharField(max_length=200)
    email = models.EmailField(blank=False, unique=True, null=False)
    phone_number = PhoneNumberField(null=True)
    timestamp =  models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    
       


# ENTITY MODEL
class Home(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True,)
    house_no =  models.CharField(max_length=200, null=True, unique=True)
    owner_name =  models.CharField(max_length=200)
    owner_email = models.EmailField(blank=False, unique=True, null=False)
    phone_number = PhoneNumberField(null=True)
    timestamp =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
























