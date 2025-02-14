import sys

import pytest
from django.test import RequestFactory

from persona_manager.admin import UserPersonaAdmin
from persona_manager.models import UserPersona
from persona_manager.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestUserPersonaAdmin:
    """
    Test suite for the UserPersonaAdmin class.
    """

    def test_activate_personas_action(
        self, user_persona_admin: UserPersonaAdmin, request_factory: RequestFactory
    ) -> None:
        """
        Test the activate_personas action.

        Asserts:
        -------
            - The is_active field is updated to True for selected personas.
        """
        user_persona = UserPersona.objects.create(
            persona_name="Test Persona", is_active=False
        )
        request = request_factory.get("/")
        user_persona_admin.activate_personas(
            request, UserPersona.objects.filter(id=user_persona.id)
        )
        user_persona.refresh_from_db()
        assert (
            user_persona.is_active
        ), "Expected is_active to be True after activating personas."

    def test_deactivate_personas_action(
        self, user_persona_admin: UserPersonaAdmin, request_factory: RequestFactory
    ) -> None:
        """
        Test the deactivate_personas action.

        Asserts:
        -------
            - The is_active field is updated to False for selected personas.
        """
        user_persona = UserPersona.objects.create(
            persona_name="Test Persona", is_active=True
        )
        request = request_factory.get("/")
        user_persona_admin.deactivate_personas(
            request, UserPersona.objects.filter(id=user_persona.id)
        )
        user_persona.refresh_from_db()
        assert (
            not user_persona.is_active
        ), "Expected is_active to be False after deactivating personas."
