from django.contrib import admin

from .models import *


# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'is_active']
    list_editable = ['url', 'is_active']


class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'position']


reg = admin.site.register

reg(SiteSetting)
reg(FooterLink, FooterLinkAdmin)
reg(FooterLinkBox)
reg(Slider, SliderAdmin)
reg(SiteBanner, BannerAdmin)
