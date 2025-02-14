import sys

import pytest
from django.test import RequestFactory
from django.urls import reverse

from persona_manager.tests.constants import PYTHON_VERSION, PYTHON_VERSION_REASON
from persona_manager.views import UserPersonaListView

pytestmark = [
    pytest.mark.views,
    pytest.mark.skipif(sys.version_info < PYTHON_VERSION, reason=PYTHON_VERSION_REASON),
]


@pytest.mark.django_db
class TestUserPersonaListView:
    """
    Test suite for the UserPersonaListView class.
    """

    def test_get_queryset_without_filter(
        self,
        user_persona_list_view: UserPersonaListView,
        create_user_personas: None,
        request_factory: RequestFactory,
    ) -> None:
        """
        Test the get_queryset method without any filters.

        Asserts:
        -------
            - The queryset includes all UserPersona instances.
        """
        request = request_factory.get(reverse("user-persona-list"))
        user_persona_list_view.request = request
        queryset = user_persona_list_view.get_queryset()
        assert (
            queryset.count() >= 2  # maybe create more instances in other tests
        ), "Expected queryset to include all UserPersona instances."

    def test_get_queryset_with_active_filter(
        self,
        user_persona_list_view: UserPersonaListView,
        create_user_personas: None,
        request_factory: RequestFactory,
    ) -> None:
        """
        Test the get_queryset method with an active filter.

        Asserts:
        -------
            - The queryset includes only active UserPersona instances.
        """
        request = request_factory.get(
            reverse("user-persona-list"), {"is_active": "true"}
        )
        user_persona_list_view.request = request
        queryset = user_persona_list_view.get_queryset()
        assert (
            queryset.count() >= 1  # maybe create more than one instance
        ), "Expected queryset to include only active UserPersona instances."
        assert (
            queryset.first().is_active
        ), "Expected the returned UserPersona to be active."

    def test_get_queryset_with_inactive_filter(
        self,
        user_persona_list_view: UserPersonaListView,
        create_user_personas: None,
        request_factory: RequestFactory,
    ) -> None:
        """
        Test the get_queryset method with an inactive filter.

        Asserts:
        -------
            - The queryset includes only inactive UserPersona instances.
        """
        request = request_factory.get(
            reverse("user-persona-list"), {"is_active": "false"}
        )
        user_persona_list_view.request = request
        queryset = user_persona_list_view.get_queryset()
        assert (
            queryset.count() <= 1  # maybe create more than one instance
        ), "Expected queryset to include only inactive UserPersona instances."
        assert (
            not queryset.first().is_active
        ), "Expected the returned UserPersona to be inactive."
