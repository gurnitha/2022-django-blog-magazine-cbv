# apps/blog/templatetags/template-library.py

# Django modules
from django import template

# Locals
from apps.blog.models import Category

# Template library
register = template.Library()

# Register your template here