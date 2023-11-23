from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from doors.models import Door, Branch, Color, CTA, Film, Panel


# Register your models here.

@admin.register(Door)
class DoorAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Color)
admin.site.register(Panel)
admin.site.register(Film)
admin.site.register(Branch)
admin.site.register(CTA)
