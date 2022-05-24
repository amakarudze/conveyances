from django.contrib import admin

from .models import Bank, ConveyanceMatter

admin.site.register(ConveyanceMatter)
admin.site.register(Bank)
