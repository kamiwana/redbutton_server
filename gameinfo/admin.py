from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(GameInfo)
admin.site.register(Movies)
admin.site.register(Subtitle)
admin.site.register(MovieDetail)
admin.site.register(GameImage)
admin.site.register(SubImage)
admin.site.register(GameFilter)
admin.site.register(GameInfoThema)