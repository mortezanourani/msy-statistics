from django.contrib import admin

from .models import City, Gender, Building_Ownership, License_Ownership

admin.site.register(City)

admin.site.register(Gender)

admin.site.register(Building_Ownership)

admin.site.register(License_Ownership)
