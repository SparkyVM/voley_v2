from django import template
from django.db.models import Count

import courts.views as views
from courts.models import Location

register = template.Library()


@register.inclusion_tag('courts/list_locations.html')
def show_location(loc_selected=0):
    locs = Location.objects.annotate(total=Count("courts")).filter(total__gt=0)
    return {'locs': locs, 'loc_selected': loc_selected}