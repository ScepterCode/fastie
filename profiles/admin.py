from django.contrib import admin
from .models import ArtisanProfile, ClientProfile, Skill, Location

@admin.register(ArtisanProfile)
class ArtisanProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_available')
    filter_horizontal = ('skills',)

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)
