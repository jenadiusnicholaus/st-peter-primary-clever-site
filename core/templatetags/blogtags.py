from django import template
from core.models import *

register = template.Library()


@register.simple_tag
def get_latest_post():
    qs = blog.objects.filter(created_on=timezone.now)[:4]
    return qs
