from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework import status
from .permissions import  IsAuthenticatedOrCreate
from .serializers import *
from member.models import Profile
from main.models import *
from etc.models import *
from django.core.mail import EmailMessage
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from etc.models import *
from .models import *

@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed", "username": username, "password": password})

    profile = Profile.objects.get(user=user)
    branch = Branch.objects.get(pk=profile.branch)

    return Response(
        {"login_id": user.id, "branch": profile.branch, "room_number": profile.room_number,"auth": profile.auth,
         "branch_name": branch.branch_name, "is_desc_request": branch.is_desc_request,"is_together":branch.is_together,"is_note":branch.is_note,
         "is_forbidden_word":branch.is_forbidden_word,"forbidden_word_cnt":branch.forbidden_word_cnt, "forbidden_word_scope":branch.forbidden_word_scope, "system_volume":branch.system_volume
         })

@api_view(['GET'])
def layer(request, branch):
    try:
        layer = Layer.objects.all().filter(branch=branch)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = LayerSerializer(layer, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def layer_sub(request, layer):
    try:
        layer_sub = LayerSub.objects.all().filter(layer=layer)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = LayerSubSerializer(layer_sub, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_list(request, branch):
    try:
        course = Course.objects.all().filter(branch=branch)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CourseSerializer(course, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def guide_movie(request, branch):
    try:
        guide = Guide.objects.get(branch=branch)
    except Guide.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GuideSerializer(guide)
    return Response(serializer.data)

@api_view(['GET'])
def gameThema_list(request):
    try:
        thema = GameThema.objects.all()
    except GameThema.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameThemaSerializer(thema, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def branchGameinfo_list(request, branch):
    try:
         queryset = GameInfo.objects.raw(
      "SELECT  b.id as id, game_id, game_name,eng_title, level, created_date, genre, genre_detail, cnt, min_cnt, max_cnt, "
      "play_time, desc_time, icon, 'desc', tag, media_cnt, setting_cnt, faq_cnt, desc_cnt, b.last_date as last_date, "
      "location, cant_explain "
      "FROM branch_gameinfo_branchgame as a, gameinfo_gameinfo as b "
      "WHERE a.gameinfo_id = b.id and a.branch_id= "+ branch + " order by id asc")

    except GameInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BranchGameInfoSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def branchGameinfo_list_v2(request, branch):
    try:
         queryset = GameInfo.objects.raw(
      "SELECT  b.id as id, game_id, game_name,eng_title, level, created_date, genre, genre_detail, cnt, min_cnt, max_cnt, "
      "play_time, desc_time, icon,'desc', tag, media_cnt, setting_cnt, faq_cnt, desc_cnt, b.last_date as last_date,"
      "location, cant_explain "
      "FROM branch_gameinfo_branchgame as a, gameinfo_gameinfo as b "
      "WHERE a.gameinfo_id = b.id and a.branch_id=" + branch + " order by id asc")

    except GameInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameInfoSerializer_v2(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def branchGameinfo_list_v3(request, branch):
    try:
         queryset = GameInfo.objects.raw(
      "SELECT  b.id as id, game_id, game_name,eng_title, level, created_date, genre, genre_detail, cnt, min_cnt, max_cnt, "
      "play_time, desc_time, icon, 'desc', tag, media_cnt, setting_cnt, faq_cnt, desc_cnt, b.last_date as last_date, "
      "location, cant_explain, b.user "
      "FROM branch_gameinfo_branchgame as a, gameinfo_gameinfo as b "
      "WHERE a.gameinfo_id = b.id AND a.is_view=1 AND a.branch_id=" + branch + " order by id asc")

    except GameInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameInfoSerializer_v3(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def gameinfoAll_list(request):
    try:
        gameinfo = GameInfo.objects.all()
    except GameInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GameInfoSerializer(gameinfo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def etc(request):
    try:
        etc = Etc.objects.get(id=1)
    except Etc.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = EtcSerializer(etc)

    return Response(serializer.data)

@api_view(['POST'])
def togetherJoinList_add(request):
    try:
        togeterJoinlist = TogeterJoinList.objects.get(branch_id=request.data.get("branch_id"),room_id=request.data.get("room_id"))
        serializer = TogetherJoinListSerializer(togeterJoinlist, data=request.data)
    except TogeterJoinList.DoesNotExist:
        serializer = TogetherJoinListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def togetherJoinList_list(request,branch_id):
    try:
        togeterJoinList = TogeterJoinList.objects.all().filter(branch_id=branch_id)
    except togeterJoinList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoinList.exists():
        serializer = TogetherJoinListSerializer(togeterJoinList, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['GET'])
def togetherJoinList_delete_branch(request,branch_id):
    try:
        togeterJoinList = TogeterJoinList.objects.all().filter(branch_id=branch_id)
    except togeterJoinList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoinList.exists():
        togeterJoinList.delete()
        return Response({"branch_id": branch_id, "delete": "ok"})
    else:
        return Response({"branch_id":branch_id,"delete":"no data"})

@api_view(['GET'])
def togetherJoinList_delete_room(request,branch_id,room_id):
    try:
        togeterJoinList = TogeterJoinList.objects.all().filter(branch_id=branch_id,room_id=room_id)
    except togeterJoinList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoinList.exists():
        togeterJoinList.delete()
        return Response({"branch_id":branch_id,"room_id:":room_id,"delete":"ok"})
    else:
        return Response({"branch_id":branch_id,"room_id:":room_id,"delete":"no data"})

@api_view(['POST'])
def togetherJoin_add(request):
    serializer = TogetherJoinSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def togetherJoin_list(request,branch_id,room_id):
    try:
        togeterJoin = TogeterJoin.objects.all().filter(recv_branch_id=branch_id,recv_room_id=room_id)
    except togeterJoin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoin.exists():
        serializer = TogetherJoinSerializer(togeterJoin, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['POST'])
def togetherJoin_list_delete(request):
    recv_branch_id = request.data.get("recv_branch_id")
    recv_room_id = request.data.get("recv_room_id")
    try:
        togeterJoin = TogeterJoin.objects.all().filter(recv_branch_id=recv_branch_id,recv_room_id=recv_room_id)
    except togeterJoin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoin.exists():
        togeterJoin.delete()
        return Response({"branch_id": recv_branch_id,"room_id": recv_room_id, "delete": "ok"})
    else:
        return Response({"branch_id":recv_branch_id,"room_id": recv_room_id, "delete":"no data"})

@api_view(['POST'])
def togetherJoin_accept_add(request):
    serializer = TogetherJoinAcceptSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def togetherJoin_accept_list(request,branch_id,room_id):
    try:
        togeterJoinAccept = TogeterJoinAccept.objects.all().filter(sender_branch_id=branch_id,sender_room_id=room_id)
    except togeterJoinAccept.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoinAccept.exists():
        serializer = TogetherJoinAcceptSerializer(togeterJoinAccept, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['POST'])
def togetherJoin_accept_list_delete(request):
    sender_branch_id = request.data.get("sender_branch_id")
    sender_room_id = request.data.get("sender_room_id")
    try:
        togeterJoinAccept = TogeterJoinAccept.objects.all().filter(sender_branch_id=sender_branch_id,sender_room_id=sender_room_id)
    except togeterJoinAccept.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterJoinAccept.exists():
        togeterJoinAccept.delete()
        return Response({"branch_id": sender_branch_id,"room_id": sender_room_id, "delete": "ok"})
    else:
        return Response({"branch_id":sender_branch_id,"room_id": sender_room_id, "delete":"no data"})

@api_view(['POST'])
def togeterMessage_add(request):
    serializer = TogeterMessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
       # if request.data.get("recv_room_id") == 999 or request.data.get("sender_room_id") == 999 :
        serializerLog = TogeterMessageLogSerializer(data=request.data)
        if serializerLog.is_valid():
            serializerLog.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def togeterMessage_list(request, branch_id, room_id):
    try:
        togeterMessage = TogeterMessage.objects.all().filter(recv_branch_id=branch_id, recv_room_id=room_id)
    except togeterMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterMessage.exists():
        serializer = TogeterMessageSerializer(togeterMessage, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['POST'])
def togeterMessage_list_delete(request):
    recv_branch_id = request.data.get("recv_branch_id")
    recv_room_id = request.data.get("recv_room_id")
    try:
        togeterMessage = TogeterMessage.objects.all().filter(recv_branch_id=recv_branch_id,recv_room_id=recv_room_id)
    except togeterMessage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if togeterMessage.exists():
        togeterMessage.delete()
        return Response({"branch_id": recv_branch_id,"room_id": recv_room_id, "delete": "ok"})
    else:
        return Response({"branch_id":recv_branch_id,"room_id": recv_room_id, "delete":"no data"})

@api_view(['POST'])
def firebase_add(request):
    try:
        firebase = FireBase.objects.get(branch_id=request.data.get("branch_id"),room_id=request.data.get("room_id"))
        serializer = FirebaseSerializer(firebase, data=request.data)
    except FireBase.DoesNotExist:
        serializer = FirebaseSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def firebase_get(request,branch_id,room_id):
    try:
        firebase = FireBase.objects.all().filter(branch_id=branch_id,room_id=room_id)
    except FireBase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if firebase.exists():
        serializer = FirebaseSerializer(firebase, many=True)
        return Response(serializer.data)
    else:
        return Response({})

@api_view(['POST'])
def sendEmail(request):
    user_id = request.data.get("login_id")
    branch_id = request.data.get("branch")
    body = request.data.get("body")

    branch = Branch.objects.get(pk=branch_id)
    subject = "[레드버튼-" + branch.branch_name + "]고객의견"
    etc = Etc.objects.get(id=1)
    data_make = {"login_id" : 1, "branch_id": branch_id, "user_id": user_id, "body": body, "mail_to": etc.mail_address}
    serializer = CustomOpinionSerializer(data=data_make)

    if serializer.is_valid():
        serializer.save()
        email = EmailMessage(
            subject,
            body,
            to=[etc.mail_address]
        )
        email.send()
        return Response(data_make, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = (IsAuthenticatedOrCreate,)

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        serializer_class = UserSerializer
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
