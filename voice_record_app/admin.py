from django.contrib import admin

# Register your models here.
from .models import Audio, Domaine

class AudioAdmin(admin.ModelAdmin):
    list_display = ('domaine', 'auteur', 'date')
    list_filter = ('domaine', 'date')
    search_fields = ('domaine__nom', 'auteur', 'date')


class DomaineAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

admin.site.register(Audio, AudioAdmin)
admin.site.register(Domaine, DomaineAdmin)
