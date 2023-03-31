from django.contrib import admin
from .models import CategoryPackage, IncludePackage, ExcludePackage, ItineraryPackage, Package


@admin.register(CategoryPackage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(IncludePackage)
class IncludeAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ExcludePackage)
class ExcludeAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(ItineraryPackage)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ['title']
