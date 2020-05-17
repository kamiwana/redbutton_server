from __future__ import unicode_literals
from django.core.validators import validate_comma_separated_integer_list
from game_thema.models import *
from game_icon.models import *
from .choices import *
import re

# Create your models here.
class GameInfo(models.Model):
    game_id = models.IntegerField(null=False, blank=False, default=0)
    #game_relation = models.ManyToManyField('GameRelation', blank=True)
    game_relation = models.CharField(max_length=255, blank=True, null=True)
    game_name = models.CharField(max_length=50, blank=False)
    genre = models.CharField(max_length=50, blank=True)
    genre_detail = models.CharField(max_length=50, blank=True)
    cnt = models.CharField(max_length=20, blank=True)
    tag = models.CharField(max_length=200, blank=False)
    desc = models.TextField(max_length=200, blank=False)
    eng_title = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=10,choices=LEVEL_TYPES)
    min_cnt = models.IntegerField(null=True, blank=False, default=0)
    max_cnt = models.IntegerField(null=True, blank=False, default=0)
    play_time = models.IntegerField(null=True, blank=False, default=0)
    desc_time = models.IntegerField(null=True, blank=False, default=0)
    icon = models.CharField(validators=[validate_comma_separated_integer_list], max_length=100, blank=True)
    media_cnt = models.IntegerField(null=True, blank=False, default=0)
    setting_cnt = models.IntegerField(null=True, blank=False, default=0)
    faq_cnt = models.IntegerField(null=True, blank=False, default=0)
    desc_cnt = models.IntegerField(null=True, blank=False, default=0)
    last_date = models.DateTimeField(auto_created=True, auto_now=True)
    user = models.CharField(max_length=150, blank=True)
    created_date = models.CharField(max_length=50, blank=False)
    game_icon = models.ManyToManyField(GameIcon, blank=True, null=True, verbose_name='아이콘')

    def __str__(self):
        return self.game_name

    def game_name_desc(self):
        try:
            qs = GameInfoDesc.objects.get(gameinfo_id=self.pk, language__code='Kor')
            game_name_desc = qs.game_name
            return game_name_desc
        except:
            return ""

    def game_genre_desc(self):
        try:
            qs = GameInfoDesc.objects.get(gameinfo_id=self.pk, language__code='Kor')
            game_genre_desc = qs.genre
            return game_genre_desc
        except:
            return ""

class GameInfoDesc(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_desc', on_delete=models.CASCADE)
    game_name = models.CharField(max_length=50, blank=False)
    genre = models.CharField(max_length=50, blank=True)
    genre_detail = models.CharField(max_length=50, blank=True)
    cnt = models.CharField(max_length=20, blank=True)
    tag = models.CharField(max_length=200, blank=False)
    desc = models.TextField(max_length=200, blank=False)
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='언어', on_delete=models.CASCADE)
    last_date = models.DateTimeField(auto_created=True, auto_now=True)

class GameImage(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='image', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/')
    div = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class Movies(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='movies', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/movies/file/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

    def __str__(self):
       return self.title

def movies_thumbnail_path(instance, filename):
    return 'gameinfo/{}/movies/{}/thumbnail/{}'.format(instance.movies.gameinfo.id, instance.movies.id, filename)

class MoviesThumbnail(models.Model):
    movies = models.ForeignKey(Movies, related_name="movies_thumbnail",  on_delete=models.CASCADE)
 #   order = models.SmallIntegerField(null=True, blank=True, default=0, verbose_name='순서')
 #   title = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to=movies_thumbnail_path, blank=True)
    time = models.CharField(max_length=20, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

    def __str__(self):
       return self.image.name

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/image/thumnail_none.png"

class Subtitle(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='subtitle', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='gameinfo/movies/subtitle/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class MovieDetail(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='movie_info', on_delete=models.CASCADE)
    movie_id = models.IntegerField(null=True, blank=False)
    subtitle_id = models.IntegerField(null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='언어', on_delete=models.CASCADE)
    language_type = models.CharField(max_length=5,choices=LANGUAGE_TYPES)
    cnt_desc = models.CharField(max_length=20)
    user = models.CharField(max_length=150, blank=True)

    def movie_file_url(self):
        try:
            movie = Movies.objects.get(id=self.movie_id)
            return movie.file.url
        except:
            return ""

    def subtitle_file_url(self):
        try:
            subtitle = Subtitle.objects.get(id=self.subtitle_id)
            return subtitle.file.url
        except:
            return ""


    def movie_file_name(self):
        try:
            movie = Movies.objects.get(id=self.movie_id)
            return movie.file.name.lstrip('gameinfo/movies/file/')
        except:
            return ""

    def subtitle_file_name(self):
        try:
            subtitle = Subtitle.objects.get(id=self.subtitle_id)
            return subtitle.file.name.lstrip('gameinfo/movies/subtitle/')
        except:
            return ""

    def language_name(self):
        if self.language is not None:
            return self.language.name
        else:
            return ""

class GameFilter(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_filters', on_delete=models.CASCADE)
    people = models.SmallIntegerField(null=True, blank=False, default=0)
    mix = models.IntegerField(null=True, blank=False, default=0)
    male = models.IntegerField(null=True, blank=False, default=0)
    female = models.IntegerField(null=True, blank=False, default=0)

class GameFilter_V2(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_filters_v2', on_delete=models.CASCADE)
    people = models.SmallIntegerField(null=True, blank=False, default=0, verbose_name='인원')
    gender = models.CharField(null=True, max_length=10, choices=GENDER_TYPE, verbose_name='구성', default=0)
    step1 = models.IntegerField(null=True, blank=False, default=0, verbose_name='워밍업')
    step2 = models.IntegerField(null=True, blank=False, default=0, verbose_name='맛보기')
    step3 = models.IntegerField(null=True, blank=False, default=0, verbose_name='본게임')
    step4 = models.IntegerField(null=True, blank=False, default=0, verbose_name='마무리')
    step5 = models.IntegerField(null=True, blank=False, default=0, verbose_name='선택해제')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=150, blank=True)

class GameInfoThema(models.Model):
    gameinfo = models.ForeignKey(GameInfo, related_name='gameinfo_thema', on_delete=models.CASCADE)
    thema = models.ManyToManyField(GameThema, related_name='game_thema')