from typing import List

from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from persona_manager.api.serializers.userpersona import UserPersonaSerializer
from persona_manager.mixins.api.config_api_attrs import ConfigureAttrsMixin
from persona_manager.mixins.api.control_api_methods import ControlAPIMethodsMixin
from persona_manager.models import UserPersona
from persona_manager.settings.conf import config


# pylint: disable=too-many-ancestors
class UserPersonaViewSet(
    GenericViewSet,
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ControlAPIMethodsMixin,
    ConfigureAttrsMixin,
):

    queryset = UserPersona.objects.all()
    serializer_class = config.persona_serializer_class or UserPersonaSerializer
    filter_backends: List = [OrderingFilter, SearchFilter]

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the viewset and configure attributes based on settings.

        Disables the 'list', 'retrieve', 'create', 'update', and 'destroy' methods
        if their corresponding settings are set to `False`.

        """
        super().__init__(*args, **kwargs)
        self.configure_attrs()

        # Mapping of configuration settings to the corresponding methods to disable
        config_method_mapping = {
            "api_allow_list": "LIST",
            "api_allow_retrieve": "RETRIEVE",
            "api_allow_create": "CREATE",
            "api_allow_update": "UPDATE",
            "api_allow_delete": "DESTROY",
        }

        # Disable methods based on configuration settings
        for config_setting, method in config_method_mapping.items():
            if not getattr(config, config_setting, True):
                self.disable_methods([method])

    def get_queryset(self):
        """Optionally filter the queryset based on query parameters."""
        queryset = super().get_queryset()

        is_active = self.request.query_params.get("is_active", None)
        if is_active in ["true", "false"]:
            queryset = queryset.filter(is_active=is_active == "true")

        return queryset
