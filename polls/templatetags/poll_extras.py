from django import template
from jalali_date import date2jalali

register =template.Library()

@register.filter(name='shamsi_date')
def get_shamsi_create_date(val):
    return date2jalali(val)


@register.filter(name='shamsi_time')
def get_shamsi_create_time(val):
    return val.strftime('%H:%H')