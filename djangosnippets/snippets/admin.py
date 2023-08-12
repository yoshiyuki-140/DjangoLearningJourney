from django.contrib import admin

# Register your models here.

from snippets.models import Snippet

admin.site.register(Snippet)
