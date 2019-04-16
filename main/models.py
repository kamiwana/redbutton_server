from django.db import models
from branch.models import Branch
from .choices import *
# Create your models here.

class Guide(models.Model):
    branch = models.ForeignKey(Branch, related_name='guide',on_delete=models.CASCADE)
    file = models.FileField(upload_to='main/guide/')
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Course(models.Model):
    branch = models.ForeignKey(Branch, related_name='course',on_delete=models.CASCADE)
    file = models.FileField(upload_to='main/course/')
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Layer(models.Model):
    branch = models.ForeignKey(Branch, related_name='layer',on_delete=models.CASCADE)
    file = models.FileField(upload_to='main/layer/')
    title = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=10, choices=LAYER_CHOICES)
    div = models.SmallIntegerField(null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class LayerSub(models.Model):
    layer = models.ForeignKey(Layer, related_name='layer_sub',on_delete=models.CASCADE)
    file = models.FileField(upload_to='main/layer/sub')
    title = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)