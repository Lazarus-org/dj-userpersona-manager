from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PersonaManagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "persona_manager"
    verbose_name = _("Django Persona Manager")
    