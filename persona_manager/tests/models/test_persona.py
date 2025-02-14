import sys

import pytest

from persona_manager.models import UserPersona
from persona_manager.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.models,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestUserPersonaModel:
    """
    Test suite for the UserPersona model.
    """

    def test_str_method(self, user_persona: UserPersona) -> None:
        """
        Test that the __str__ method returns the correct string representation of an announcement category.

        Asserts:
        -------
            - The string representation of the announcement category includes the name.
        """
        expected_str = user_persona.persona_name
        assert (
            str(user_persona) == expected_str
        ), f"Expected the __str__ method to return '{expected_str}', but got '{str(user_persona)}'."
