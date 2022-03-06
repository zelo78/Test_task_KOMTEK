from django.contrib import admin

from main.models import Record, Resource, ResourceIdentifier


class VersionInline(admin.StackedInline):
    model = Resource
    extra = 0


class ResourceIdentifierAdmin(admin.ModelAdmin):
    list_display = ['value']
    inlines = [VersionInline]


admin.site.register(ResourceIdentifier, ResourceIdentifierAdmin)


class RecordInline(admin.TabularInline):
    model = Record
    extra = 1


class ResourceAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'version', 'valid_from', 'identifier']
    inlines = [RecordInline]


admin.site.register(Resource, ResourceAdmin)


class RecordAdmin(admin.ModelAdmin):
    list_display = ['code', 'value', 'resource']


admin.site.register(Record, RecordAdmin)
