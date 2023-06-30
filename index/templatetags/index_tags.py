from django import template
from ..models import Header, Footer, RequestPage

register = template.Library()

# @register.inclusion_tag('index/includes/header.html', takes_context=True)
@register.simple_tag()
def header_config():
    return Header.objects.first()


@register.simple_tag()
def footer_config():
    return Footer.objects.first()


# @register.simple_tag()
# def contact_config():
#     return RequestPage.objects.first()
