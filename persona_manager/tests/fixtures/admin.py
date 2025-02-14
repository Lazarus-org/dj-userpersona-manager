import pytest
from django.contrib.admin import AdminSite
from django.test import RequestFactory

from persona_manager.admin import UserPersonaAdmin
from persona_manager.models import UserPersona


@pytest.fixture
def request_factory() -> RequestFactory:
    """
    Fixture to provide an instance of RequestFactory.

    Returns:
    -------
        RequestFactory: An instance of Django's RequestFactory.
    """
    return RequestFactory()


@pytest.fixture
def admin_site() -> AdminSite:
    """
    Fixture to provide an instance of AdminSite.

    Returns:
    -------
        AdminSite: An instance of Django's AdminSite.
    """
    return AdminSite()


@pytest.fixture
def user_persona_admin(admin_site: AdminSite) -> UserPersonaAdmin:
    """
    Fixture to provide an instance of UserPersonaAdmin.

    Args:
    ----
        admin_site (AdminSite): An instance of Django's AdminSite.

    Returns:
    -------
        UserPersonaAdmin: An instance of UserPersonaAdmin.
    """
    return UserPersonaAdmin(UserPersona, admin_site)
