from django.contrib import admin

from .models import *


# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']

class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url','is_active']
    list_editable = ['url','is_active']


admin.site.register(SiteSetting)
admin.site.register(FooterLink, FooterLinkAdmin)
admin.site.register(FooterLinkBox)
admin.site.register(Slider, SliderAdmin)
