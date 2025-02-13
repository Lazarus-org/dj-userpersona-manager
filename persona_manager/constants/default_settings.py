from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class DefaultImageSettings:
    validators: Optional[List] = None
    upload_path: str = "persona_images/"


@dataclass(frozen=True)
class DefaultAdminSettings:
    admin_site_class: Optional[str] = None


@dataclass(frozen=True)
class DefaultThrottleSettings:
    authenticated_user_throttle_rate: str = "30/minute"
    staff_user_throttle_rate: str = "100/minute"
    throttle_class: str = "persona_manager.api.throttlings.RoleBasedUserRateThrottle"


@dataclass(frozen=True)
class DefaultPaginationAndFilteringSettings:
    pagination_class: str = (
        "persona_manager.api.paginations.DefaultLimitOffSetPagination"
    )
    ordering_fields: List[str] = field(
        default_factory=lambda: [
            "id",
            "persona_name",
            "created_at",
            "updated_at",
        ]
    )
    search_fields: List[str] = field(
        default_factory=lambda: ["persona_name", "description"]
    )


# pylint: disable=too-many-instance-attributes
@dataclass(frozen=True)
class DefaultAPISettings:
    allow_list: bool = True
    allow_retrieve: bool = True
    allow_create: bool = False
    allow_update: bool = False
    allow_delete: bool = False
    extra_permission_class: Optional[str] = None
    parser_classes: List[str] = field(
        default_factory=lambda: [
            "rest_framework.parsers.JSONParser",
            "rest_framework.parsers.MultiPartParser",
            "rest_framework.parsers.FormParser",
        ]
    )
    persona_serializer_class = None


image_settings = DefaultImageSettings()
admin_settings = DefaultAdminSettings()
throttle_settings = DefaultThrottleSettings()
pagination_and_filter_settings = DefaultPaginationAndFilteringSettings()
api_settings = DefaultAPISettings()
