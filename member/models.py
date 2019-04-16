from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.encoding import python_2_unicode_compatible
from .choices import *
from django.conf import settings

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch = models.CharField(max_length=20, null=True, blank=True)
    room_number = models.IntegerField(null=True, blank=True, default=0)
    auth = models.PositiveSmallIntegerField(choices=AUTH_CHOICES, null=True, blank=True)
    phone_number= models.CharField(max_length=20, null=True, blank=True)
    login_user = models.CharField(max_length=150, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def auth_verbose(self):
        return get_display(self.auth, AUTH_CHOICES)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return False

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

def get_display(key, list):
    d = dict(list)
    if key in d:
        return d[key]
    return None