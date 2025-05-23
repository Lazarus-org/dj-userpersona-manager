from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from persona_manager.models import UserPersona
from persona_manager.settings.conf import config


@admin.register(UserPersona, site=config.admin_site_class)
class UserPersonaAdmin(admin.ModelAdmin):
    list_display = ("persona_name", "is_active", "created_at", "updated_at")
    list_editable = ("is_active",)
    list_filter = ("is_active", "created_at", "updated_at")
    list_per_page = 10
    search_fields = ("persona_name", "description")
    date_hierarchy = "created_at"
    actions = ("activate_personas", "deactivate_personas")
    fieldsets = (
        (None, {"fields": ("persona_name", "description", "is_active", "image")}),
        (
            _("Advanced Options"),
            {
                "fields": ("attributes",),
                "classes": ("collapse",),
            },
        ),
    )

    def activate_personas(self, request, queryset):
        queryset.update(is_active=True)

    activate_personas.short_description = _("Activate selected personas")

    def deactivate_personas(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_personas.short_description = _("Deactivate selected personas")
