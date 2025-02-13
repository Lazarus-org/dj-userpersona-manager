import pytest

from persona_manager.models import UserPersona


@pytest.fixture
def user_persona() -> UserPersona:
    """
    Fixture to create a UserPersona instance.
    """
    return UserPersona.objects.create(persona_name="Test persona")