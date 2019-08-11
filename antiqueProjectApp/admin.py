from django.contrib import admin

# Register your models here.
from antiqueProjectApp.models import Creator, AntiqueType, Antique, AntiqueSale

# admin.site.register(Antique)
admin.site.register(Creator)
admin.site.register(AntiqueType)
admin.site.register(AntiqueSale)


@admin.register(Antique)
class AntiqueAdmin(admin.ModelAdmin):
   list_display = ('AntiqueName', 'Creator', 'display_AntiqueType')
