# Ex02 Django ORM Web Application
## Date: 23.10.25

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
admin.py

from django.contrib import admin
from . models import MOVIES, MOVIESAdmin

# Register your models here.
admin.site.register(MOVIES, MOVIESAdmin)

models.py

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
```

## OUTPUT

![alt text](<tej/tej/Screenshot 2025-10-23 105047.png>)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully.
