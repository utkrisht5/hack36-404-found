from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Victim)
admin.site.register(Authority)
admin.site.register(Complain)