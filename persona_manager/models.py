from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    ImageField,
    JSONField,
    Model,
    TextField,
)
from django.utils.translation import gettext_lazy as _

from persona_manager.settings.conf import config


class UserPersona(Model):
    image = ImageField(
        verbose_name=_("Image"),
        upload_to=config.image_upload_path,
        help_text=_("An image representing the user persona."),
        db_comment="Stores an image representing the user persona.",
        validators=config.image_validators or [],
        blank=True,
        null=True,
    )
    persona_name = CharField(
        verbose_name=_("Persona Name"),
        max_length=100,
        help_text=_("The name of the user persona."),
        db_comment="Stores the name of the user persona.",
    )
    description = TextField(
        verbose_name=_("Description"),
        help_text=_("A detailed description of the user persona."),
        db_comment="Stores a detailed description of the user persona.",
        blank=True,
        null=True,
    )
    is_active = BooleanField(
        verbose_name=_("Is Active"),
        help_text=_("Indicates whether the user persona is active."),
        db_comment="Indicates whether the user persona is active.",
        default=True,
    )
    created_at = DateTimeField(
        verbose_name=_("Created At"),
        help_text=_("The date and time when the user persona was created."),
        db_comment="Stores the date and time when the user persona was created.",
        auto_now_add=True,
    )
    updated_at = DateTimeField(
        verbose_name=_("Updated At"),
        help_text=_("The date and time when the user persona was last updated."),
        db_comment="Stores the date and time when the user persona was last updated.",
        auto_now=True,
    )
    attributes = JSONField(
        verbose_name=_("Attributes"),
        help_text=_("Additional attributes specific to the user persona."),
        db_comment="Stores additional attributes specific to the user persona.",
        default=dict,
        blank=True,
    )

    def __str__(self):
        return self.persona_name

    class Meta:
        db_table = "user_personas"
        verbose_name = _("User Persona")
        verbose_name_plural = _("User Personas")
