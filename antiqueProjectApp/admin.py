from django.contrib import admin
from antiqueProjectApp.models import Creator, AntiqueType, Antique, AntiqueSale
from antiqueProjectApp.models import AntiqueSale

admin.site.register(Creator)
admin.site.register(AntiqueType)


@admin.register(Antique)
class AntiqueAdmin(admin.ModelAdmin):
   list_display = ('AntiqueName', 'Creator', 'display_AntiqueType')

@admin.register(AntiqueSale)
class AntiqueSaleAdmin(admin.ModelAdmin):
    list_display = ('customerFirstName', 'customerLastName')
    list_filter = ('saleDate',)
