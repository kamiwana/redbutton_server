from django.db import models

# Create your models here.django_migrations

class Branch(models.Model):
    branch_code = models.CharField(max_length=10,blank=False)
    branch_name = models.CharField(max_length=20,blank=False)
    branch_user = models.CharField(max_length=20, null=True, blank=True)
    branch_address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    game_cnt = models.IntegerField(null=True, blank=True, default=0)
    is_together = models.BooleanField()
    is_note = models.BooleanField()
    is_forbidden_word= models.BooleanField()
    is_desc_request = models.BooleanField()
    forbidden_word_cnt=models.IntegerField(null=True, blank=True, default=0)
    forbidden_word_scope = models.IntegerField(null=True, blank=True, default=0)
    system_volume = models.IntegerField(null=True, blank=True, default=0)
    user = models.CharField(max_length=150, null=True, blank=True)
    last_date = models.DateTimeField(auto_created=True,auto_now=True)
    class Meta:
        ordering = ['-branch_code']
