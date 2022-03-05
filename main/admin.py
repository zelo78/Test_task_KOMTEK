from django.contrib import admin

from main.models import Record, Resource, ResourceVersion


class VersionInline(admin.StackedInline):
    model = ResourceVersion
    extra = 0


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['identifier', 'short_name']
    inlines = [VersionInline]


admin.site.register(Resource, ResourceAdmin)


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1


class ResourceVersionAdmin(admin.ModelAdmin):
    inlines = [RecordInline]


admin.site.register(ResourceVersion, ResourceVersionAdmin)
admin.site.register(Record)
