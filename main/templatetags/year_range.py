# main/templatetags/year_range.py
from django import template
from datetime import datetime

register = template.Library()

@register.simple_tag
def year_range(start_year):
    current_year = datetime.now().year
    return f"{start_year}-{current_year}" if current_year > start_year else str(start_year)