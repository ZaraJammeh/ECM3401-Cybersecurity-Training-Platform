from django.contrib import admin

from .models import GapFillText, GapFillOption

class GapFillOptionInline(admin.TabularInline):
    model = GapFillOption
    extra = 3

class GapFillTextAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            "Activity Details",
            {"classes": ["collapse"], "fields":["estim_min_duration", "estim_max_duration", "tags"]}
        ),
        (
            "Gap Fill Text",
            {"fields":["text"]}
        ),
    ]
    inlines = [GapFillOptionInline]
    
admin.site.register(GapFillText, GapFillTextAdmin)