from django.contrib import admin

from .models import Bank, ConveyanceMatter, Matter

admin.site.register(ConveyanceMatter)
admin.site.register(Bank)
admin.site.register(Matter)
