from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class UserPersona(models.Model):
    image = models.ImageField(
        upload_to='persona_images/',
        blank=True,
        null=True,
        help_text=_("An image representing the user persona."),
        db_comment="Stores an image representing the user persona."
    )
    persona_name = models.CharField(
        max_length=100,
        help_text=_("The name of the user persona."),
        db_comment="Stores the name of the user persona."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text=_("A detailed description of the user persona."),
        db_comment="Stores a detailed description of the user persona."
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("Indicates whether the user persona is active."),
        db_comment="Indicates whether the user persona is active."
    )
    image = models.ImageField(
        upload_to='persona_images/',
        blank=True,
        null=True,
        help_text=_("An image representing the user persona."),
        db_comment="Stores an image representing the user persona."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time when the user persona was created."),
        db_comment="Stores the date and time when the user persona was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("The date and time when the user persona was last updated."),
        db_comment="Stores the date and time when the user persona was last updated."
    )
    attributes = models.JSONField(
        default=dict,
        blank=True,
        help_text=_("Additional attributes specific to the user persona."),
        db_comment="Stores additional attributes specific to the user persona."
    )

    def __str__(self):
        return self.persona_name

    class Meta:
        db_table = 'user_personas'
        verbose_name = _('User Persona')
        verbose_name_plural = _('User Personas')
        db_table_comment = "Stores information about user personas, including their names, descriptions, images, and attributes."