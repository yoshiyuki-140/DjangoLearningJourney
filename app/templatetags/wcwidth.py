from django.template import Library
from wcwidth import wcswidth as func_wcswidth

register = Library()

@register.filter(is_safe=True)
def wcswidth(value):
    if not isinstance(value,str):
        return 0
    return func_wcswidth(value)
