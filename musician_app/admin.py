from django.contrib import admin
from .models import Instrument_Model, Musician_Model

# Register your models here.
admin.site.register(Instrument_Model)
admin.site.register(Musician_Model)
