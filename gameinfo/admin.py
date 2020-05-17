from django.contrib import admin
from .models import *
from django import forms
from game_icon.models import *

from django.utils.safestring import mark_safe

class Movies_Admin(admin.ModelAdmin):
    # Post 객체를 보여줄 때 출력할 필드 설정
    list_display = ('game_id', 'game_name', 'file_link', )
    #search_fields = ('gameinfo.game_name', 'game_id',)
    list_per_page = 1000

    def file_link(self, obj):
        if obj.file:
            return mark_safe("<a href='{}' download>{}s</a>".format(obj.file.url, obj.file.name))
        else:
            return "No attachment"

    file_link.short_description = 'File Download'

    def game_name(self, obj):
        return obj.gameinfo.game_name
    def game_id(self, obj):
        return obj.gameinfo.game_id

    game_id.admin_order_field = 'gameinfo__game_id'

admin.site.register(Movies, Movies_Admin)

class GameInfoForm(forms.ModelForm):
    game_icon = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=GameIcon.objects.all())

class GameFilter_V2_Admin(admin.ModelAdmin):
    # Post 객체를 보여줄 때 출력할 필드 설정
    list_display = ('people', 'step1', 'step2', 'step3', 'step4', 'step5', 'uploaded_at')

class GameFilter_V2lnline(admin.TabularInline):
    model = GameFilter_V2
    fk_name = 'gameinfo'

class GameDesc_Inline(admin.TabularInline):
    model = GameInfoDesc
    fk_name = 'gameinfo'

class GameInfoAdmin(admin.ModelAdmin):
    form = GameInfoForm
    inlines = [GameFilter_V2lnline, GameDesc_Inline, ]

admin.site.register(GameInfo, GameInfoAdmin)
admin.site.register(Subtitle)
admin.site.register(MovieDetail)
admin.site.register(GameImage)
admin.site.register(GameFilter)
admin.site.register(GameInfoThema)
admin.site.register(MoviesThumbnail)
admin.site.register(GameFilter_V2, GameFilter_V2_Admin)