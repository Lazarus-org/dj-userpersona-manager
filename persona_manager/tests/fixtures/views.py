import pytest
from rest_framework.test import APIClient

from persona_manager.models import UserPersona
from persona_manager.views import UserPersonaListView


@pytest.fixture
def user_persona_list_view() -> UserPersonaListView:
    """
    Fixture to provide an instance of UserPersonaListView.

    Returns:
    -------
        UserPersonaListView: An instance of UserPersonaListView.
    """
    return UserPersonaListView()


@pytest.fixture
def create_user_personas() -> None:
    """
    Fixture to create test UserPersona instances.

    Returns:
    -------
        None
    """
    UserPersona.objects.create(persona_name="Active Persona", is_active=True)
    UserPersona.objects.create(persona_name="Inactive Persona", is_active=False)


@pytest.fixture
def api_client() -> APIClient:
    """
    Fixture to initialize the Django REST Framework APIClient for testing.

    :return: An instance of APIClient to make HTTP requests in tests.
    """
    return APIClient()
