from gameinfo.models import *
from branch_gameinfo.models import *
from main.models import *
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from etc.models import *
from togeter.models import *
from game_thema.models import *

class CourseListSerializer(serializers.ListSerializer):

    @property
    def data(self):
        # call the super() to get the default serialized data
        serialized_data =  super(CourseListSerializer, self).data
        course_representation = {'data': serialized_data} # insert the above response in a dictionary
        return course_representation

class EtcSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Etc
        fields = ('mail_address','movie_watch_cnt','volume_settting',)

class LayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layer
        fields = ('file','type','div','pk')

    file = serializers.ReadOnlyField(source='file.url')

class LayerSubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Layer
        fields = ('file',)

    file = serializers.ReadOnlyField(source='file.url')

class GuideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = ('file',)

    file = serializers.ReadOnlyField(source='file.url')


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class ItemsSerializer(serializers.Serializer):
    items = serializers.ListField(child=ItemSerializer())

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.ReadOnlyField(source='file.url')

    class Meta:
        model = Course
        fields = ('file',)
        list_serializer_class = CourseListSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

# 사용자 그룹
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class SubtitleSerializer(serializers.ModelSerializer):
    file = serializers.ReadOnlyField(source='file.url')

    class Meta:
        model = Movies
        fields = ('file',)

class MoviesSerializer(serializers.ModelSerializer):
    file = serializers.ReadOnlyField(source='file.url')
    class Meta:
        model = Movies
        fields = ('file',)

class MovieField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        id = super(MovieField, self).to_representation(value)
        try:
          movie = Movies.objects.get(pk=id)
          serializer = MoviesSerializer(movie)
          return serializer.data
        except movie.DoesNotExist:
            return None

class SubtitleField(serializers.PrimaryKeyRelatedField):

    def to_representation(self, value):
        if self.pk_field is not None:
            id = super(SubtitleField, self).to_representation(value)
            try:
              subtitle = Subtitle.objects.get(pk=id)
              serializer = MoviesSerializer(subtitle)
              return serializer.data
            except subtitle.DoesNotExist:
                return []
        return {"file": ''}

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_id = MovieField(queryset=Movies.objects.all())
    subtitle_id = SubtitleField(queryset=Subtitle.objects.all())

    class Meta:
        model = MovieDetail
        fields = ('movie_id','subtitle_id', 'cnt_desc', 'language_type',)

class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameImage
        fields = ('div','file',)

class BranchGameSerializer(serializers.ModelSerializer):

    class Meta:
        model = BranchGame
        fields = ('location',)


class GameInfoSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)
    movie_info = MovieDetailSerializer(many=True)

    class Meta:
        model = GameInfo
        fields = ('__all__')


class TogetherJoinListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogeterJoinList
        fields = ('__all__')

class TogetherJoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogeterJoin
        fields = ('__all__')

class TogetherJoinAcceptSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogeterJoinAccept
        fields = ('__all__')

class TogeterMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogeterMessage
        fields = ('__all__')

class TogeterMessageLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TogeterMessageLog
        fields = ('__all__')

class FirebaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = FireBase
        fields = ('__all__')

class CustomOpinionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomOpinion
        fields = ('__all__')

class GameFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameFilter
        fields = ('people', 'mix', 'male', 'female',)

class GameThemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameThema
        fields = ('__all__')

class GameInfoThemaSerializer(serializers.ModelSerializer):

    thema = GameThemaSerializer(many=True, read_only=True)

    class Meta:
        model = GameInfoThema
        fields = ('thema',)

class BranchGameInfoSerializer(serializers.Serializer):
    id=serializers.IntegerField(required=True)
    game_id = serializers.IntegerField(required=True)
    game_name = serializers.CharField(max_length=50)
    eng_title = serializers.CharField(max_length=50)
    level = serializers.CharField(max_length=10)
    created_date = serializers.CharField(max_length=50)
    genre = serializers.CharField(max_length=50)
    genre_detail = serializers.CharField(max_length=50)
    cnt = serializers.CharField(max_length=20)
    min_cnt = serializers.IntegerField(required=True)
    max_cnt = serializers.IntegerField(required=True)
    play_time = serializers.IntegerField(required=False)
    desc_time = serializers.IntegerField(required=False)
    icon = serializers.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    desc = serializers.CharField(max_length=200)
    tag = serializers.CharField(max_length=200)
    media_cnt = serializers.IntegerField(required=False)
    setting_cnt = serializers.IntegerField(required=False)
    faq_cnt = serializers.IntegerField(required=False)
    desc_cnt = serializers.IntegerField(required=False)
    last_date = serializers.DateTimeField()
    location = serializers.CharField(max_length=50)
    cant_explain = serializers.IntegerField(required=False)
    movie_info = MovieDetailSerializer(many=True)
    image = ImageSerializer(many=True)

    class Meta:

        fields = ("__all__")

class GameInfoSerializer_v2(serializers.ModelSerializer):

    image = ImageSerializer(many=True)
    movie_info = MovieDetailSerializer(many=True)
    gameinfo_filters = GameFilterSerializer(many=True)
    gameinfo_thema = GameInfoThemaSerializer(many=True)


    class Meta:
        model = GameInfo
        fields = ('__all__')


class GameInfoSerializer_v3(serializers.ModelSerializer):

    id=serializers.IntegerField(required=True)
    game_id = serializers.IntegerField(required=True)
    game_name = serializers.CharField(max_length=50)
    eng_title = serializers.CharField(max_length=50)
    level = serializers.CharField(max_length=10)
    created_date = serializers.CharField(max_length=50)
    genre = serializers.CharField(max_length=50)
    genre_detail = serializers.CharField(max_length=50)
    cnt = serializers.CharField(max_length=20)
    min_cnt = serializers.IntegerField(required=True)
    max_cnt = serializers.IntegerField(required=True)
    play_time = serializers.IntegerField(required=False)
    desc_time = serializers.IntegerField(required=False)
    icon = serializers.CharField(validators=[validate_comma_separated_integer_list], max_length=100)
    desc = serializers.CharField(max_length=200)
    tag = serializers.CharField(max_length=200)
    media_cnt = serializers.IntegerField(required=False)
    setting_cnt = serializers.IntegerField(required=False)
    faq_cnt = serializers.IntegerField(required=False)
    desc_cnt = serializers.IntegerField(required=False)
    last_date = serializers.DateTimeField()
    location = serializers.CharField(max_length=50)
    cant_explain = serializers.IntegerField(required=False)
    user = serializers.CharField(max_length=150)

    image = ImageSerializer(many=True)
    movie_info = MovieDetailSerializer(many=True)
    gameinfo_filters = GameFilterSerializer(many=True)
    gameinfo_thema = GameInfoThemaSerializer(many=True)


    class Meta:
        model = GameInfo
        fields = ('__all__')