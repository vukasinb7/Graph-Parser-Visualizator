# myapp/templatetags/myapp_filters.py

from django import template

register = template.Library()


@register.filter
def append(values, arg):
    new_value = []
    for value in values:
        new_value.append(value)
    new_value.append(arg)
    return new_value
