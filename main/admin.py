from django.contrib import admin

from main import models


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'short_name']


admin.site.register(models.Resource, ResourceAdmin)
admin.site.register(models.ResourceVersion)
admin.site.register(models.Record)
