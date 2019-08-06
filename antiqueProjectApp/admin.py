from django.contrib import admin

# Register your models here.
from antiqueProjectApp.models import Creator, AntiqueType, Antique

#admin.site.register(Antique)
admin.site.register(Creator)
admin.site.register(AntiqueType)

@admin.register(Antique)
class AntiqueAdmin(admin.ModelAdmin):
    list_display = ('Antique', 'Creator', 'display_AntiqueType')