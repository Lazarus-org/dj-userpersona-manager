import sys
from unittest.mock import Mock
from urllib.parse import urlencode

import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.test import APIClient

from persona_manager.models import UserPersona
from persona_manager.settings.conf import config
from persona_manager.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON

pytestmark = [
    pytest.mark.api,
    pytest.mark.api_views,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


class TestUserPersonaViewSet:
    """Test suite for the UserPersonaViewSet class."""

    def test_list_personas(
        self,
        api_client: APIClient,
        admin_user: User,
        monkeypatch: Mock,
        user_persona: UserPersona,
    ):
        """
        Test the list view of the UserPersonaViewSet.
        Ensures that users can list personas.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_allow_list = True  # Ensure the list method is allowed

        url = reverse("user-persona-list")
        response = api_client.get(url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert "results" in response.data, "Expected 'results' in response data."
        assert len(response.data["results"]) > 0, "Expected personas in the results."

    def test_retrieve_persona(
        self,
        api_client: APIClient,
        admin_user: User,
        user_persona: UserPersona,
    ):
        """
        Test the retrieve view of the UserPersonaViewSet.
        Ensures that staff users and non-staff users can retrieve a specific persona.
        """
        api_client.force_authenticate(user=admin_user)

        config.api_allow_retrieve = True  # Ensure the retrieve method is allowed
        config.exclude_serializer_empty_fields = True  # Testing this option too

        url = reverse("user-persona-detail", kwargs={"pk": user_persona.pk})

        # Test the filter method
        query_params = {"is_active": "true"}
        full_url = f"{url}?{urlencode(query_params)}"
        response = api_client.get(full_url)

        assert (
            response.status_code == 200
        ), f"Expected 200 OK, got {response.status_code}."
        assert (
            response.data["id"] == user_persona.pk
        ), f"Expected UserPersona ID {user_persona.pk}, got {response.data['id']}."

    @pytest.mark.parametrize("is_staff", [True, False])
    def test_list_personas_disabled(
        self, api_client: APIClient, admin_user: User, user: User, is_staff: bool
    ):
        """
        Test the list view when disabled via configuration.
        """
        _user = admin_user if is_staff else user
        api_client.force_authenticate(user=_user)

        config.api_allow_list = False  # Disable the list method

        url = reverse("user-persona-list")
        response = api_client.get(url)

        assert (
            response.status_code == 405
        ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    def test_retrieve_persona_disabled(
        self,
        api_client: APIClient,
        admin_user: User,
        user: User,
        user_persona,
    ):
        """
        Test the retrieve view when disabled via configuration.
        """
        for user in [admin_user, user]:
            api_client.force_authenticate(user=user)

            config.api_allow_retrieve = False  # Disable the retrieve method
            config.api_extra_permission_class = AllowAny  # Also test this config

            url = reverse("user-persona-detail", kwargs={"pk": user_persona.pk})
            response = api_client.get(url)

            assert (
                response.status_code == 405
            ), f"Expected 405 Method Not Allowed, got {response.status_code}."

    # def test_serializer_class_selection(
    #     self,
    #     api_client: APIClient,
    #     admin_user: User,
    #     user: User,
    #     user_persona,
    # ):
    #     """
    #     Test that the appropriate serializer class is selected based on the user role.
    #     """
    #     for user, expected_serializer in [
    #         (admin_user, "UserPersonaSerializer"),
    #         (user, "SimplepersonaSerializer"),
    #     ]:
    #         api_client.force_authenticate(user=user)
    #
    #         config.api_allow_retrieve = True  # Ensure the retrieve method is allowed
    #
    #         url = reverse("user-persona-detail", kwargs={"pk": user_persona.pk})
    #         response = api_client.get(url)
    #
    #         assert (
    #             response.status_code == 200
    #         ), f"Expected 200 OK, got {response.status_code}."
    #         assert "id" in response.data, f"Expected announcement ID in the response."
    #         # Check if the correct serializer is used (based on the fields present)
    #         if user.is_staff:
    #             assert (
    #                 "audience" in response.data
    #             ), "Expected 'audience' in the detailed serializer."
    #         else:
    #             assert (
    #                 "audience" not in response.data
    #             ), "Expected 'audience' not to be present in the simple serializer."
