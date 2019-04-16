from django.db import models

class TogeterJoinList(models.Model):
    branch_id  = models.IntegerField(null=False, blank=False)
    room_id = models.IntegerField(null=False, blank=False)
    man_count = models.IntegerField(null=False, blank=True)
    woman_count = models.IntegerField(null=False, blank=True)
    our_ages = models.CharField(max_length=50, blank=True)
    req_person_count = models.IntegerField(null=False, blank=True)
    req_gender = models.IntegerField(null=False, blank=True)
    req_age_begin =models.IntegerField(null=False, blank=True)
    req_age_end =models.IntegerField(null=False, blank=True)
    specials = models.CharField(max_length=255, blank=True)
    our_age_begin_idx = models.IntegerField(null=True, blank=True)
    our_age_end_idx = models.IntegerField(null=True, blank=True)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)

class TogeterJoin(models.Model):
    sender_branch_id  = models.IntegerField(null=False, blank=False)
    sender_room_id = models.IntegerField(null=False, blank=False)
    recv_branch_id  = models.IntegerField(null=False, blank=False)
    recv_room_id = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)

class TogeterJoinAccept(models.Model):
    sender_branch_id  = models.IntegerField(null=False, blank=False)
    sender_room_id = models.IntegerField(null=False, blank=False)
    recv_branch_id  = models.IntegerField(null=False, blank=False)
    recv_room_id = models.IntegerField(null=False, blank=False)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)

class TogeterMessage(models.Model):
    sender_branch_id  = models.IntegerField(null=False, blank=False)
    sender_room_id = models.IntegerField(null=False, blank=False)
    recv_branch_id  = models.IntegerField(null=False, blank=False)
    recv_room_id = models.IntegerField(null=False, blank=False)
    msg = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)

class FireBase(models.Model):
    branch_id  = models.IntegerField(null=False, blank=False)
    room_id = models.IntegerField(null=False, blank=False)
    firebase_id=models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)

class TogeterMessageLog(models.Model):
    sender_branch_id  = models.IntegerField(null=False, blank=False)
    sender_room_id = models.IntegerField(null=False, blank=False)
    recv_branch_id  = models.IntegerField(null=False, blank=False)
    recv_room_id = models.IntegerField(null=False, blank=False)
    msg = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_created=True, auto_now=True)