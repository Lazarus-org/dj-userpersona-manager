import sys
from unittest.mock import MagicMock, patch

import pytest

from persona_manager.settings.checks import check_persona_settings
from persona_manager.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.settings,
    pytest.mark.settings_checks,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestCheckPersonaSettings:
    @patch("persona_manager.settings.checks.config")
    def test_valid_settings(self, mock_config: MagicMock) -> None:
        """
        Test that valid settings produce no errors.

        Args:
        ----
            mock_config (MagicMock): Mocked configuration object with valid settings.

        Asserts:
        -------
            No errors are returned when all settings are valid.
        """
        # Mock the config values to be valid
        mock_config.api_allow_list = True
        mock_config.api_allow_retrieve = False
        mock_config.api_allow_create = False
        mock_config.api_allow_update = False
        mock_config.api_allow_delete = False
        mock_config.image_upload_path = "test_path/"
        mock_config.image_validators = []
        mock_config.api_ordering_fields = ["created_at"]
        mock_config.api_search_fields = ["id"]
        mock_config.staff_user_throttle_rate = "10/minute"
        mock_config.authenticated_user_throttle_rate = "5/minute"
        mock_config.get_setting.side_effect = lambda name, default: None

        errors = check_persona_settings(None)

        # There should be no errors for valid settings
        assert not errors

    @patch("persona_manager.settings.checks.config")
    def test_invalid_boolean_settings(self, mock_config: MagicMock) -> None:
        """
        Test that invalid boolean settings return errors.

        Args:
        ----
            mock_config (MagicMock): Mocked configuration object with invalid boolean settings.

        Asserts:
        -------
            Three errors are returned for invalid boolean values in settings.
        """
        # Mock the config values with invalid boolean settings
        mock_config.api_ordering_fields = ["created_at"]
        mock_config.api_search_fields = ["id"]
        mock_config.staff_user_throttle_rate = "10/minute"
        mock_config.authenticated_user_throttle_rate = "5/minute"
        mock_config.api_allow_list = "not_boolean"
        mock_config.api_allow_retrieve = "not_boolean"
        mock_config.api_allow_create = "not_boolean"
        mock_config.api_allow_update = "not_boolean"
        mock_config.api_allow_delete = "not_boolean"
        mock_config.image_upload_path = "test_path/"
        mock_config.image_validators = []
        mock_config.get_setting.side_effect = lambda name, default: None

        errors = check_persona_settings(None)

        # Expect 5errors for invalid boolean values
        assert len(errors) == 5
        assert (
            errors[0].id
            == f"persona_manager.E001_{mock_config.prefix}API_ALLOW_LIST"
        )
        assert (
            errors[1].id
            == f"persona_manager.E001_{mock_config.prefix}API_ALLOW_RETRIEVE"
        )
        assert (
                errors[2].id
                == f"persona_manager.E001_{mock_config.prefix}API_ALLOW_CREATE"
        )
        assert (
                errors[3].id
                == f"persona_manager.E001_{mock_config.prefix}API_ALLOW_UPDATE"
        )
        assert (
                errors[4].id
                == f"persona_manager.E001_{mock_config.prefix}API_ALLOW_DELETE"
        )

    @patch("persona_manager.settings.checks.config")
    def test_invalid_list_settings(self, mock_config: MagicMock) -> None:
        """
        Test that invalid list settings return errors.

        Args:
        ----
            mock_config (MagicMock): Mocked configuration object with invalid list settings.

        Asserts:
        -------
            Three errors are returned for invalid list values in settings.
        """
        # Mock the config values with invalid list settings
        mock_config.api_allow_list = True
        mock_config.api_allow_retrieve = False
        mock_config.api_allow_create = False
        mock_config.api_allow_update = False
        mock_config.api_allow_delete = False
        mock_config.api_ordering_fields = []
        mock_config.image_upload_path = "test_path/"
        mock_config.image_validators = []
        mock_config.staff_user_throttle_rate = "10/minute"
        mock_config.authenticated_user_throttle_rate = "5/minute"
        mock_config.get_setting.side_effect = lambda name, default: None
        mock_config.api_search_fields = [123]  # Invalid list element

        errors = check_persona_settings(None)

        # Expect 2 errors for invalid list settings
        assert len(errors) == 2
        assert (
            errors[0].id
            == f"persona_manager.E003_{mock_config.prefix}API_ORDERING_FIELDS"
        )
        assert (
            errors[1].id
            == f"persona_manager.E004_{mock_config.prefix}API_SEARCH_FIELDS"
        )

    @patch("persona_manager.settings.checks.config")
    def test_invalid_throttle_rate(self, mock_config: MagicMock) -> None:
        """
        Test that invalid throttle rates return errors.

        Args:
        ----
            mock_config (MagicMock): Mocked configuration object with invalid throttle rates.

        Asserts:
        -------
            Two errors are returned for invalid throttle rates.
        """
        # Mock the config values with invalid throttle rates
        mock_config.api_allow_list = True
        mock_config.api_allow_retrieve = False
        mock_config.api_allow_create = False
        mock_config.api_allow_update = False
        mock_config.api_allow_delete = False
        mock_config.image_upload_path = "test_path/"
        mock_config.image_validators = []
        mock_config.api_ordering_fields = ["created_at"]
        mock_config.api_search_fields = ["id"]
        mock_config.staff_user_throttle_rate = "invalid_rate"
        mock_config.authenticated_user_throttle_rate = "abc/hour"
        mock_config.get_setting.side_effect = lambda name, default: None

        errors = check_persona_settings(None)

        # Expect 2 errors for invalid throttle rates
        assert len(errors) == 2
        assert errors[0].id == "persona_manager.E005"
        assert errors[1].id == "persona_manager.E007"

    @patch("persona_manager.settings.checks.config")
    def test_invalid_path_import(self, mock_config: MagicMock) -> None:
        """
        Test that invalid path import settings return errors.

        Args:
        ----
            mock_config (MagicMock): Mocked configuration object with invalid paths.

        Asserts:
        -------
            Seven errors are returned for invalid path imports.
        """
        # Mock the config values with invalid paths
        mock_config.api_allow_list = True
        mock_config.api_allow_retrieve = False
        mock_config.api_allow_create = False
        mock_config.api_allow_update = False
        mock_config.api_allow_delete = False
        mock_config.api_ordering_fields = ["created_at"]
        mock_config.api_search_fields = ["id"]
        mock_config.staff_user_throttle_rate = "10/minute"
        mock_config.authenticated_user_throttle_rate = "5/minute"
        mock_config.image_upload_path = []  # invalid,should be str
        mock_config.get_setting.side_effect = (
            lambda name, default: "invalid.path.ClassName"
        )

        errors = check_persona_settings(None)

        # Expect 8 errors for invalid path imports
        assert len(errors) == 8

        assert (
                errors[0].id
                == f"persona_manager.E014_{mock_config.prefix}IMAGE_UPLOAD_PATH"
        )
        assert (
            errors[1].id
            == f"persona_manager.E010_{mock_config.prefix}API_THROTTLE_CLASS"
        )
        assert (
            errors[2].id
            == f"persona_manager.E010_{mock_config.prefix}API_PERSONA_SERIALIZER_CLASS"
        )
        assert (
            errors[3].id
            == f"persona_manager.E010_{mock_config.prefix}API_PAGINATION_CLASS"
        )
        assert (
            errors[4].id
            == f"persona_manager.E011_{mock_config.prefix}API_PARSER_CLASSES"
        )
        assert (
                errors[5].id
                == f"persona_manager.E011_{mock_config.prefix}IMAGE_VALIDATORS"
        )
        assert (
            errors[6].id
            == f"persona_manager.E010_{mock_config.prefix}API_EXTRA_PERMISSION_CLASS"
        )
        assert (
            errors[7].id
            == f"persona_manager.E010_{mock_config.prefix}ADMIN_SITE_CLASS"
        )
