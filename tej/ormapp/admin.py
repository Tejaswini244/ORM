from django.contrib import admin
from . models import MOVIES, MOVIESAdmin

# Register your models here.
admin.site.register(MOVIES, MOVIESAdmin)