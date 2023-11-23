from django.contrib import admin

from doors.models import Door, Branch, Color, CTA, Film, Panel

# Register your models here.

admin.site.register(Door)

class DoorAdmin(admin.ModelAdmin):
    fieldsets = (
        ("", {
            'fields': ()
        })
    )

admin.site.register(Color)
admin.site.register(Panel)
admin.site.register(Film)
admin.site.register(Branch)
admin.site.register(CTA)

