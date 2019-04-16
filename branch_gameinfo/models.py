from django.db import models
from gameinfo.models import GameInfo
# Create your models here.
class BranchGame(models.Model):
    branch = models.ForeignKey('branch.Branch', related_name='branch',on_delete=models.CASCADE)
    gameinfo = models.ForeignKey('gameinfo.GameInfo', related_name='gameinfo_branch',on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=True)
    last_date = models.DateTimeField(auto_created=True,auto_now=True)
    user = models.CharField(max_length=150, blank=True)
    is_view = models.BooleanField(default=0)
    cant_explain = models.BooleanField(default=0)