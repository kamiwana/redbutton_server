from django.contrib import admin

# Register your models here.

from .models import *

# Register your models here.

admin.site.register(Guide)
admin.site.register(Course)
admin.site.register(Layer)
admin.site.register(LayerSub)
