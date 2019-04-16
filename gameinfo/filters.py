import django_filters
from.models import Movies,Subtitle,MovieDetail

class MovieDetailFilter(django_filters.FilterSet):
    class Meta:
        model = MovieDetail
        fields = ['cnt', 'language_type', 'movie_id','subtitle_id', ]

    def __init__(self,gameinfo_id,*args, **kwargs):

        super(MovieDetailFilter, self).__init__(*args, **kwargs)
        movie_list = Movies.objects.all().filter(gameinfo_id=gameinfo_id)
        subtitle_list = Subtitle.objects.all().filter(gameinfo_id=gameinfo_id)
        movie_choices = [(o.pk, str(o.file)) for o in movie_list]
        subtitle_choices = [(o.pk, str(o.file)) for o in subtitle_list]

        self.fields['movie_id'] = Movies.objects.values('file').filter(id = movie_id)
        self.fields['subtitle_id'] = Subtitle.objects.values('file').filter(id=subtitle_id)
