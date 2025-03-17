from django.contrib import admin

from .models import GapFillText, GapFillOption

class GapFillOptionInline(admin.TabularInline):
    model = GapFillOption
    extra = 3

class GapFillTextInline(admin.ModelAdmin):
    inlines = [GapFillOptionInline]
admin.site.register(GapFillText, GapFillTextInline)