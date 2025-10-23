from django.db import models
from django.contrib import admin

# Create your models here.
class MOVIES(models.Model):
    MOVIE_id = models.IntegerField(primary_key=True)
    MOVIE_name = models.CharField(max_length=50)
    MOVIE_AMOUNT = models.CharField(max_length=50)
    MOVIE_SCREEN = models.IntegerField()
    MOVIE_DATE = models.DateField()

class MOVIESAdmin(admin.ModelAdmin):
    list_display = ('MOVIE_id','MOVIE_name','MOVIE_AMOUNT','MOVIE_SCREEN','MOVIE_DATE')