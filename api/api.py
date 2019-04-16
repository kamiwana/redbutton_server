from rest_framework import generics, permissions
from .serializers import *
from gameinfo.models import *
from rest_framework import generics
# from .permissions import IsAuthenticatedOrCreate,IsOwnerOrReadOnly

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
  #  permission_classes = (IsAuthenticatedOrCreate,)

class Login(generics.RetrieveAPIView):
    queryset = User.objects.all().first()
    serializer_class = UserSerializer

class MoviesoMixin(object):
    model = Movies
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MoviesList(MoviesoMixin,generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]

class GameInfoMixin(object):
    model = GameInfo
    queryset = GameInfo.objects.all().filter()
    serializer_class = GameInfoSerializer

class GameInfoList(GameInfoMixin,generics.ListCreateAPIView):
    permission_classes = [
        permissions.AllowAny
    ]