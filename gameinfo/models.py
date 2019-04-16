from __future__ import unicode_literals
from django.db import models
from .choices import *
from django.core.validators import validate_comma_separated_integer_list
from game_thema.models import *

# Create your models here.
class GameInfo(models.Model):
    game_id = models.IntegerField(null=False, blank=False, default=0)
    game_name = models.CharField(max_length=50, blank=False)
    eng_title = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=10,choices=LEVEL_TYPES)
    created_date =  models.CharField(max_length=50, blank=False)
    genre = models.CharField(max_length=50, blank=True)
    genre_detail = models.CharField(max_length=50, blank=True)
    cnt = models.CharField(max_length=20, blank=True)
    min_cnt=models.IntegerField(null=True, blank=False, default=0)
    max_cnt = models.IntegerField(null=True, blank=False, default=0)
    play_time=models.IntegerField(null=True, blank=False, default=0)
    desc_time = models.IntegerField(null=True, blank=False, default=0)
    icon = models.CharField(validators=[validate_comma_separated_integer_list],max_length=100, blank=True)
    desc = models.TextField(max_length=200, blank=False)
    tag = models.CharField(max_length=200, blank=False)
    media_cnt = models.IntegerField(null=True, blank=False, default=0)
    setting_cnt = models.IntegerField(null=True, blank=False, default=0)
    faq_cnt = models.IntegerField(null=True, blank=False, default=0)
    desc_cnt = models.IntegerField(null=True, blank=False, default=0)
    last_date = models.DateTimeField(auto_created=True,auto_now=True)
    user = models.CharField(max_length=150, blank=True)

class GameImage(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='image',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/')
    div = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Movies(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='movies',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/movies/file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Subtitle(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='subtitle',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/movies/subtitle/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class MovieDetail(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='movie_info',on_delete=models.CASCADE)
    movie_id = models.IntegerField(null=True, blank=False)
    subtitle_id = models.IntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    language_type = models.CharField(max_length=5,choices=LANGUAGE_TYPES)
    cnt_desc = models.CharField(max_length=20)
    user = models.CharField(max_length=150, blank=True)

class SubImage(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_subimage',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/subimage/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Setting(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_setting',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/setting/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class FAQ(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_faq',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/faq/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Desc(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_desc',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/desc/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Summary(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_summary',on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/summary/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class GameFilter(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_filters', on_delete=models.CASCADE)
    people = models.SmallIntegerField(null=True, blank=False, default=0)
    mix = models.IntegerField(null=True, blank=False, default=0)
    male = models.IntegerField(null=True, blank=False, default=0)
    female = models.IntegerField(null=True, blank=False, default=0)

class GameInfoThema(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_thema', on_delete=models.CASCADE)
    thema = models.ManyToManyField(GameThema, related_name='game_thema')