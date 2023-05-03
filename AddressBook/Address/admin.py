from django.contrib import admin

# Register your models here.
from .models import Voivodeship, Address
admin.site.register(Voivodeship)
admin.site.register(Address)