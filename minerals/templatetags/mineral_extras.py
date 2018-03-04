from django import template
from random import randint
from django.utils.safestring import mark_safe

import markdown2

from minerals.models import Mineral

register = template.Library()


groups = ["Silicates", "Oxides", "Sulfates", "Sulfides", "Carbonates", "Halides",
            "Sulfosalts", "Phosphates", "Borates", "Organic Minerals", "Arsenates",
            "Native Elements", "Other"]


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    """Converts markdown text to HTML for organic compounds"""
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)


@register.filter(name='random_mineral')
def random_mineral(mineral):
    """Returns a random mineral from all availible options in database"""
    minerals = len(Mineral.objects.all())
    mineral = randint(1, minerals)
    return mineral


@register.inclusion_tag('minerals_nav.html')
def nav_minerals_list():
    return {'groups': groups}
