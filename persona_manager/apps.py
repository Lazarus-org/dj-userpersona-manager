from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PersonaManagerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "persona_manager"
    verbose_name = _("Django Persona Manager")

    def ready(self):
        """This method is called when the application is fully loaded.

        Its main purpose is to perform startup tasks, such as importing
        and registering system checks for validating the configuration
        settings of the `persona_manager` app. It ensures that
        all necessary configurations are in place and properly validated
        when the Django project initializes.

        In this case, it imports the settings checks from the
        `persona_manager.settings` module to validate the configuration
        settings.

        """
        from persona_manager.settings import checks
