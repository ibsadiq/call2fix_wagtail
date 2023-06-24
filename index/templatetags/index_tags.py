from django import template
from ..models import Header

register = template.Library()

# @register.inclusion_tag('index/includes/header.html', takes_context=True)
@register.simple_tag()
def header_config():
    return Header.objects.first()

