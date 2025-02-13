from typing import Any, List

from django.conf import settings
from django.utils.module_loading import import_string

from persona_manager.constants.default_settings import (
    admin_settings,
    api_settings,
    image_settings,
    pagination_and_filter_settings,
    throttle_settings,
)
from persona_manager.constants.types import DefaultPath, OptionalPaths


# pylint: disable=too-many-instance-attributes
class PersonaManagerConfig:
    """A configuration handler.

    allowing dynamic settings loading from the Django settings, with
    default fallbacks.

    """

    prefix = "PERSONA_MANAGER_"

    def __init__(self) -> None:
        self.image_upload_path: str = self.get_setting(
            f"{self.prefix}IMAGE_UPLOAD_PATH",
            image_settings.upload_path,
        )
        self.image_validators: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}IMAGE_VALIDATORS",
            image_settings.validators,
        )

        self.api_allow_list: bool = self.get_setting(
            f"{self.prefix}API_ALLOW_LIST", api_settings.allow_list
        )
        self.api_allow_retrieve: bool = self.get_setting(
            f"{self.prefix}API_ALLOW_RETRIEVE",
            api_settings.allow_retrieve,
        )
        self.api_allow_create: bool = self.get_setting(
            f"{self.prefix}API_ALLOW_CREATE",
            api_settings.allow_create,
        )
        self.api_allow_update: bool = self.get_setting(
            f"{self.prefix}API_ALLOW_UPDATE",
            api_settings.allow_update,
        )
        self.api_allow_delete: bool = self.get_setting(
            f"{self.prefix}API_ALLOW_DELETE",
            api_settings.allow_delete,
        )
        self.authenticated_user_throttle_rate: str = self.get_setting(
            f"{self.prefix}AUTHENTICATED_USER_THROTTLE_RATE",
            throttle_settings.authenticated_user_throttle_rate,
        )
        self.staff_user_throttle_rate: str = self.get_setting(
            f"{self.prefix}STAFF_USER_THROTTLE_RATE",
            throttle_settings.staff_user_throttle_rate,
        )
        self.api_throttle_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_THROTTLE_CLASS",
            throttle_settings.throttle_class,
        )
        self.api_pagination_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_PAGINATION_CLASS",
            pagination_and_filter_settings.pagination_class,
        )
        self.api_extra_permission_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_EXTRA_PERMISSION_CLASS",
            api_settings.extra_permission_class,
        )
        self.api_parser_classes: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_PARSER_CLASSES",
            api_settings.parser_classes,
        )
        self.persona_serializer_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}API_PERSONA_SERIALIZER_CLASS",
            api_settings.persona_serializer_class,
        )
        self.api_ordering_fields: List[str] = self.get_setting(
            f"{self.prefix}API_ORDERING_FIELDS",
            pagination_and_filter_settings.ordering_fields,
        )
        self.api_search_fields: List[str] = self.get_setting(
            f"{self.prefix}API_SEARCH_FIELDS",
            pagination_and_filter_settings.search_fields,
        )
        self.admin_site_class: OptionalPaths = self.get_optional_paths(
            f"{self.prefix}ADMIN_SITE_CLASS",
            admin_settings.admin_site_class,
        )

    def get_setting(self, setting_name: str, default_value: Any) -> Any:
        """Retrieve a setting from Django settings with a default fallback.

        Args:
            setting_name (str): The name of the setting to retrieve.
            default_value (Any): The default value to return if the setting is not found.

        Returns:
            Any: The value of the setting or the default value if not found.

        """
        return getattr(settings, setting_name, default_value)

    def get_optional_paths(
        self,
        setting_name: str,
        default_path: DefaultPath,
    ) -> OptionalPaths:
        """Dynamically load a method or class path on a setting, or return None
        if the setting is None or invalid.

        Args:
            setting_name (str): The name of the setting for the method or class path.
            default_path (Optional[Union[str, List[str]]): The default import path for the method or class.

        Returns:
            Optional[Union[Type[Any], List[Type[Any]]]]: The imported method or class or None
             if import fails or the path is invalid.

        """
        _path: DefaultPath = self.get_setting(setting_name, default_path)

        if _path and isinstance(_path, str):
            try:
                return import_string(_path)
            except ImportError:
                return None
        elif _path and isinstance(_path, list):
            try:
                return [import_string(path) for path in _path if isinstance(path, str)]
            except ImportError:
                return []

        return None


# Create a global config object
config: PersonaManagerConfig = PersonaManagerConfig()
