from django.contrib import admin

from .models import Bank, ConveyanceMatter, Matter


class ConveyanceMatterAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'bank',
        'complete',
        'created_at',
        'last_updated'
    )
    list_filter = ('bank',)
    search_fields = (
        'bank',
    )
    readonly_fields = (
        'created_by',
        'created_at',
        'last_updated'
    )


class MatterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created_at',
        'last_updated',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    readonly_fields = (
        'last_updated',
        'created_at',
    )


class BankAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = ('name',)
    search_fields = (
        'name',
    )
    
admin.site.register(ConveyanceMatter, ConveyanceMatterAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Matter, MatterAdmin)
