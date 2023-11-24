from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Branch, Film, Color, Panel, Door, CTA


class PanelInline(admin.StackedInline):
    model = Panel
    extra = 1


class ColorInline(admin.TabularInline):
    model = Door.colors.through
    extra = 1


class FilmInline(admin.TabularInline):
    model = Door.films.through
    extra = 1


@admin.register(Branch)
class BranchAdmin(ImportExportModelAdmin):
    list_display = ('name',)


@admin.register(Film)
class FilmAdmin(ImportExportModelAdmin):
    list_display = ('name', 'image_thumbnail')

    def image_thumbnail(self, obj):
        return obj.image.url if obj.image else ''

    image_thumbnail.short_description = 'Thumbnail'


@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    list_display = ('name', 'color_preview')

    def color_preview(self, obj):
        return f'<div style="width: 30px; height: 30px; background-color: {obj.hex_value}"></div>'

    color_preview.short_description = 'Preview'
    color_preview.allow_tags = True


@admin.register(Panel)
class PanelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'image')


@admin.register(Door)
class DoorAdmin(ImportExportModelAdmin):
    list_display = ('title', 'branch', 'description', 'inside_img', 'outside_img', 'price', 'popular')
    inlines = [ColorInline, FilmInline]
    search_fields = ('title', 'description')
    list_filter = ('branch', 'colors', 'films')
    list_display_links = ('title',)
    list_per_page = 20

@admin.register(CTA)
class CTAAdmin(ImportExportModelAdmin):
    list_display = ('title', 'subtitle', 'door', 'show')
    list_filter = ('door', 'show')


# Если вы хотите настроить просмотр истории с помощью simple_history
class DoorHistoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'history_date', 'history_type', 'history_user')
