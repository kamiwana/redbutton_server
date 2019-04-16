from django.db import models

class Etc(models.Model):
    mail_address = models.CharField(max_length=255,blank=False,null=True)
    movie_watch_cnt = models.IntegerField(null=True, blank=True,default=1)
    volume_settting = models.IntegerField(null=True, blank=True,default=1)
    uploaded_at = models.DateTimeField(auto_created=True,auto_now=True)
    user = models.CharField(max_length=150, blank=True)

class CustomOpinion(models.Model):
    branch_id = models.IntegerField(null=True, blank=True)
    user_id = models.CharField(max_length=150,blank=False,null=True)
    body = models.TextField(null=False)
    uploaded_at = models.DateTimeField(auto_created=True,auto_now=True)