from django.db import models

# Create your models here.
class GameThema(models.Model):
    thema_name = models.CharField(max_length=50, blank=False)
    thema_order = models.SmallIntegerField(blank=True)

    class Meta:
        ordering = ['thema_order']

    def __str__(self):
        return self.thema_name