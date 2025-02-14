# Django UserPersona Manager
[![License](https://img.shields.io/github/license/lazarus-org/dj-userpersona-manager)](https://github.com/lazarus-org/dj-userpersona-manager/blob/main/LICENSE)
[![PyPI Release](https://img.shields.io/pypi/v/dj-userpersona-manager)](https://pypi.org/project/dj-userpersona-manager/)
[![Pylint Score](https://img.shields.io/badge/pylint-10/10-brightgreen?logo=python&logoColor=blue)](https://www.pylint.org/)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/dj-userpersona-manager)](https://pypi.org/project/dj-userpersona-manager/)
[![Supported Django Versions](https://img.shields.io/pypi/djversions/dj-userpersona-manager)](https://pypi.org/project/dj-userpersona-manager/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=yellow)](https://github.com/pre-commit/pre-commit)
[![Open Issues](https://img.shields.io/github/issues/lazarus-org/dj-userpersona-manager)](https://github.com/lazarus-org/dj-userpersona-manager/issues)
[![Last Commit](https://img.shields.io/github/last-commit/lazarus-org/dj-userpersona-manager)](https://github.com/lazarus-org/dj-userpersona-manager/commits/main)
[![Languages](https://img.shields.io/github/languages/top/lazarus-org/dj-userpersona-manager)](https://github.com/lazarus-org/dj-userpersona-manager)
[![Coverage](https://codecov.io/gh/lazarus-org/dj-userpersona-manager/branch/main/graph/badge.svg)](https://codecov.io/gh/lazarus-org/dj-userpersona-manager)

[`dj-userpersona-manager`](https://github.com/lazarus-org/dj-userpersona-manager/) is a Django package developed by Lazarus to manage user personas efficiently. It provides a `UserPersona` model to store persona details, a Django `ModelAdmin` for easy management via the admin panel, and a built-in template list view for viewing personas. Additionally, it offers an optional Django REST Framework (DRF) API for persona management at the API level.

This package is designed to be flexible and easy to integrate into Django projects, allowing developers to categorize and manage different user personas effectively. Whether you need a simple admin-based solution or a full-fledged API, `dj-userpersona-manager` provides the necessary tools to streamline persona management.



## Project Detail

- Language: Python >= 3.9
- Framework: Django >= 4.2
- Django REST Framework: >= 3.14


## Documentation Overview

The documentation is organized into the following sections:

- **[Quick Start](#quick-start)**: Get up and running quickly with basic setup instructions.
- **[API Guide](#api-guide)**: Detailed information on available APIs and endpoints.
- **[Usage](#usage)**: How to effectively use the package in your projects.
- **[Settings](#settings)**: Configuration options and settings you can customize.


---


# Quick Start

This section provides a fast and easy guide to getting the `dj-userpersona-manager` package up and running in your Django project.
Follow the steps below to quickly set up the package and start managing user persona.

## 1. Install the Package

**Option 1: Using `pip` (Recommended)**

Install the package via pip:

```bash
$ pip install dj-userpersona-manager
```
**Option 2: Using `Poetry`**

If you're using Poetry, add the package with:

```bash
$ poetry add dj-userpersona-manager
```

**Option 3: Using `pipenv`**

If you're using pipenv, install the package with:

```bash
$ pipenv install dj-userpersona-manager
```

## 2. Install Django REST Framework (Optional for API Support)

If you plan to use the optional DRF API for managing personas, you will need to install Django REST Framework. If it's not already installed in your project, you can install it via pip:

**Using pip:**

```bash
$ pip install djangorestframework
```

## 3. Add to Installed Apps

After installing the necessary packages, ensure that both `rest_framework` (if using the API) and `persona_manager` are added to the `INSTALLED_APPS` in your Django `settings.py` file:

```python
INSTALLED_APPS = [
   # ...
   "rest_framework",  # Only needed if using the API

   "persona_manager",
   # ...
]
```

## 4. Apply Migrations

Run the following command to apply the necessary migrations:
```shell
python manage.py migrate
```

## 5. Add UserPersona API URLs

If you wish to use the optional API or the Django Template View Include them in your project’s `urls.py` file:
```python
from django.urls import path, include
from persona_manager.views import UserPersonaListView

urlpatterns = [
    # ...
    path("userpersona/", UserPersonaListView.as_view(), name="user-persona-list"), # Template View
    path("api/", include("persona_manager.api.routers.main")),   # Only needed if using the API
    # ...
]
```

----

# API Guide

This section provides a detailed overview of the Django UserPersona Manager API, allowing users to manage User Persona efficiently. The API exposes two main endpoints:


## UserPersona API

The ``api/userpersona/`` endpoint provides the following features:

- **List User Persona**:

  Fetches all User Personas. Controlled by the ``PERSONA_MANAGER_API_ALLOW_LIST`` setting.

- **Create a user persona**:

  Creates a new User Persona. This feature is controlled by the ``PERSONA_MANAGER_API_ALLOW_CREATE`` setting.

- **Update a user persona**:

  Updates an existing User Persona by its ID. This feature is controlled by the ``PERSONA_MANAGER_API_ALLOW_UPDATE`` setting.


- **Delete a user persona**:

  Deletes a specific User Persona by its ID. This feature is controlled by the ``PERSONA_MANAGER_API_ALLOW_DELETE`` setting.


---

## Example Responses

Here are some examples of responses for each action:


**List user persona with default serializer**:

```text
GET /api/userpersona/

Response:
HTTP/1.1 200 OK
Content-Type: application/json

"results": [
    {
            "id": 1,
            "image": "http://127.0.0.1:8000/media/persona_images/img.png",
            "persona_name": "some name",
            "description": "some desc",
            "is_active": true,
            "created_at": "2025-02-10T19:00:39.044847Z",
            "updated_at": "2025-02-10T19:31:10.772769Z",
            "attributes": {}
        },
        {
            "id": 2,
            "image": null,
            "persona_name": "some name",
            "description": "desc",
            "is_active": false,
            "created_at": "2025-02-10T19:04:30.170044Z",
            "updated_at": "2025-02-11T08:01:39.529855Z",
            "attributes": {}
        }
]
```

---

## Throttling

The API includes a built-in throttling mechanism that limits the number of requests a user can make based on their role. You can customize these throttle limits in the settings file.

To specify the throttle rates for authenticated users and staff members, add the following in your settings:

```ini
PERSONA_MANAGER_AUTHENTICATED_USER_THROTTLE_RATE = "100/day"
PERSONA_MANAGER_STAFF_USER_THROTTLE_RATE = "60/minute"
```

These settings limit the number of requests users can make within a given timeframe.

**Note:** You can define custom throttle classes and reference them in your settings.

---

## Filtering, Ordering, and Search

The API supports filtering, ordering, and searching of personas. filtering can be applied optionally, allowing users to narrow down results.

Options include:

- **Filtering**: filtering is applicable using query params, by passing `is_active` which can be `true` or `false`. Example: `/api/userpersona/?is_active=true`.

- **Ordering**: Results can be ordered by fields such as `id`, `persona_name`, `created_at` or `updated_at`.

- **Search**: You can search fields like ``persona_name`` and ``description``.

These fields can be customized by adjusting the related configurations in your Django settings.

---

## Pagination

The API supports limit-offset pagination, with configurable minimum, maximum, and default page size limits. This controls the number of results returned per page.

---

## Permissions

The base permission for all endpoints is ``IsAuthenticated``, meaning users must be logged in to access the API. You can extend this by creating custom permission classes to implement more specific access control.

For instance, you can allow only specific user roles to perform certain actions.

---

## Parser Classes

The API supports multiple parser classes that control how data is processed. The default parsers include:

- ``JSONParser``
- ``MultiPartParser``
- ``FormParser``

You can modify parser classes by updating the API settings to include additional parsers or customize the existing ones to suit your project.

----

Each feature can be configured through the Django settings file. For further details, refer to the [Settings](#settings) section.

# Usage

This section provides a comprehensive guide on how to utilize the package's key features, including the functionality of the Django admin panels for managing user personas.

## Admin Site

If you are using a **custom admin site** in your project, you must pass your custom admin site configuration in your Django settings. Otherwise, Django may raise the following error during checks or the ModelAdmin will not accessible in the Admin panel.

To resolve this, In your ``settings.py``, add the following setting to specify the path to your custom admin site class instance

```python
PERSONA_MANAGER_ADMIN_SITE_CLASS = "path.to.your.custom.site"
```

example of a custom Admin Site:

```python
from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
  site_header = "Custom Admin"
  site_title = "Custom Admin Portal"
  index_title = "Welcome to the Custom Admin Portal"


# Instantiate the custom admin site as example
example_admin_site = CustomAdminSite(name="custom_admin")
```

and then reference the instance like this:

```python
PERSONA_MANAGER_ADMIN_SITE_CLASS = "path.to.example_admin_site"
```

This setup allows `dj-userpersona-manager` to use your custom admin site for its Admin interface, preventing any errors and ensuring a smooth integration with the custom admin interface.

## UserPersona Admin Panel

The `UserPersonaAdmin` class provides a comprehensive admin interface for managing user personas in the Django admin panel. The features and functionality are described below:

### List Display

The list view for user personas includes the following fields:

- `Persona Name`: The name of the user persona.
- `Active Status`: Displays whether the persona is active (`True` or `False`).
- `Created at`: The creation time of the persona.
- `Updated at`: The last updated time of the persona.

This view helps admins get a quick overview of the user personas and their current status.

### Editing in List View

Admins can directly edit the `Active Status` (whether a persona is active) from the list view by clicking on the checkbox in the `Active Status` column.

### Filtering

Admins can filter the list of personas based on the following fields:

- `Active Status`: Filter by whether the persona is active or not.
- `Created at`: Filter by the creation time of the persona.
- `Updated at`: Filter by the last updated time.

These filters make it easier to find specific personas based on their status or time-related attributes.

### Search Functionality

Admins can search for user personas using the following fields:

- `Persona Name`: The name of the persona.
- `Description`: A description of the persona.

This search functionality enables quick access to specific personas by key identifiers.

### Pagination

The admin list view displays **10 personas per page** by default. This helps improve load times and makes it easier for admins to manage large lists of personas.

### Actions

The `UserPersonaAdmin` includes custom actions to manage personas:

- **Activate selected personas**: This action allows admins to activate multiple personas at once. It updates the `is_active` field to `True`.
- **Deactivate selected personas**: This action allows admins to deactivate multiple personas at once. It updates the `is_active` field to `False`.

### Fieldsets

The `UserPersonaAdmin` is divided into two sections:

1. **Basic Information**: This section includes fields for `persona_name`, `description`, `is_active`, and `image`.
2. **Advanced Options**: This collapsible section contains the `attributes` field for more detailed persona information.

These fieldsets help organize the admin interface for easier management of personas.

----

## UserPersona Template List View

The `UserPersonaListView` class provides a simple way to display the list of user personas in a template. It uses Django's `ListView` to automatically manage the display and pagination of the personas.

### Features

- **Template**: The list is rendered using the `userpersona_list.html` template, which you can customize according to your needs.
- **Context**: The personas are passed to the template as a variable named `personas`.
- **Filtering**: The list view allows optional filtering based on the `is_active` query parameter. If `is_active=true` or `is_active=false` is passed in the URL, the personas will be filtered accordingly.

### Customizing the List View

You can customize the queryset further by modifying the `get_queryset` method. The current implementation allows filtering by `is_active` status, but you can extend it to include other filters based on your requirements.

### Adding the URL

To include the `UserPersonaListView` in your project, add the following URL pattern to your `urls.py`:

```python
from django.urls import path
from persona_manager.views import UserPersonaListView

urlpatterns = [
    # Other URL patterns
    path("personas/", UserPersonaListView.as_view(), name="user-persona-list"),
    # Other URL patterns
]

```

# Settings

This section outlines the available settings for configuring the `dj-userpersona-manager` package. You can customize these settings in your Django project's `settings.py` file to tailor the behavior of the user persona manager system to your needs.

## Example Settings

Below is an example configuration with default values:

```python

PERSONA_MANAGER_ADMIN_SITE_CLASS = None
PERSONA_MANAGER_API_PERSONA_SERIALIZER_CLASS = None
PERSONA_MANAGER_API_ALLOW_LIST = True
PERSONA_MANAGER_API_ALLOW_RETRIEVE = False
PERSONA_MANAGER_API_ALLOW_CREATE = False
PERSONA_MANAGER_API_ALLOW_UPDATE = False
PERSONA_MANAGER_API_ALLOW_DELETE = False
PERSONA_MANAGER_IMAGE_VALIDATORS = []
PERSONA_MANAGER_IMAGE_UPLOAD_PATH = "persona_images/"
PERSONA_MANAGER_AUTHENTICATED_USER_THROTTLE_RATE = "30/minute"
PERSONA_MANAGER_STAFF_USER_THROTTLE_RATE = "100/minute"
PERSONA_MANAGER_API_THROTTLE_CLASS = (
    "persona_manager.api.throttlings.role_base_throttle.RoleBasedUserRateThrottle"
)
PERSONA_MANAGER_API_PAGINATION_CLASS = "persona_manager.api.paginations.limit_offset_pagination.DefaultLimitOffSetPagination"
PERSONA_MANAGER_API_EXTRA_PERMISSION_CLASS = None
PERSONA_MANAGER_API_PARSER_CLASSES = [
    "rest_framework.parsers.JSONParser",
    "rest_framework.parsers.MultiPartParser",
    "rest_framework.parsers.FormParser",
]
PERSONA_MANAGER_API_ORDERING_FIELDS = [
    "id",
    "persona_name",
    "created_at",
    "updated_at",
]
PERSONA_MANAGER_API_SEARCH_FIELDS = ["persona_name", "description"]
```

## Settings Overview

Below is a detailed description of each setting, so you can better understand and tweak them to fit your project's needs.


### ``PERSONA_MANAGER_ADMIN_SITE_CLASS``

**Type**: ``Optional[str]``

**Default**: ``None``

**Description**: Optionally specifies A custom AdminSite class to apply on Admin interface. This allows for more customization on Admin interface, enabling you to apply your AdminSite class into `dj-userpersona-manager` Admin interface.

---

### ``PERSONA_MANAGER_API_ALLOW_LIST``

**Type**: ``bool``

**Default**: ``True``

**Description**: Allows the listing of user persona via the API. Set to ``False`` to disable this feature.

---

### ``PERSONA_MANAGER_API_ALLOW_RETRIEVE``

**Type**: ``bool``

**Default**: ``True``

**Description**: Allows retrieving individual persona_manager via the API. Set to ``False`` to disable this feature.

---

### ``PERSONA_MANAGER_API_ALLOW_CREATE``

**Type**: ``bool``

**Default**: ``False``

**Description**: Allows the creating a user persona via the API. Set to ``True`` to enable this feature.

---

### ``PERSONA_MANAGER_API_ALLOW_UPDATE``

**Type**: ``bool``

**Default**: ``False``

**Description**: Allows updating a user persona via the API. Set to ``True`` to enable this feature.

---

### ``PERSONA_MANAGER_API_ALLOW_DELETE``

**Type**: ``bool``

**Default**: ``False``

**Description**: Allow deleting a user persona via the API. Set to ``True`` to enable this feature.

---

### ``PERSONA_MANAGER_IMAGE_VALIDATORS``

**Type**: ``list``

**Default**: ``[]`` (empty list)

**Description**: Allows specifying a list of additional validators for images files in user personas. Each validator should be passed as a Python path string, which can be dynamically loaded and applied to the image. For example, to add custom file size or file type validation, include paths to custom validator functions or classes.

----

### ``PERSONA_MANAGER_IMAGE_UPLOAD_PATH``

**Type**: ``str``

**Default**: ``"persona_images/"``

**Description**: Specifies the upload path for images files in user personas.

---

### ``PERSONA_MANAGER_AUTHENTICATED_USER_THROTTLE_RATE``

**Type**: ``str``

**Default**: ``"30/minute"``

**Description**: Sets the throttle rate (requests per minute, hour or day) for authenticated users in the API.

---

### ``PERSONA_MANAGER_STAFF_USER_THROTTLE_RATE``

**Type**: `str`

**Default**: `"100/minute"`

**Description**: Sets the throttle rate (requests per minute, hour or day) for staff (Admin) users in the API.

---

### ``PERSONA_MANAGER_API_THROTTLE_CLASS``

**Type**: ``str``

**Default**: ``"persona_manager.api.throttlings.role_base_throttle.RoleBasedUserRateThrottle"``

**Description**:  Specifies the throttle class used to limit API requests. Customize this or set it to ``None`` if no throttling is needed or want to use ``rest_framework`` `DEFAULT_THROTTLE_CLASSES`.

---

### ``PERSONA_MANAGER_API_PERSONA_SERIALIZER_CLASS``

**Type**: ``str``

**Default**: ``"persona_manager.api.serializers.userpersona.UserPersonaSerializer"``

**Description**: Defines the serializer class used in the API. Customize this if you prefer a different serializer class.


---

### ``PERSONA_MANAGER_API_PAGINATION_CLASS``

**Type**: ``str``

**Default**: ``"persona_manager.api.paginations.limit_offset_pagination.DefaultLimitOffSetPagination"``

**Description**: Defines the pagination class used in the API. Customize this if you prefer a different pagination style or set to ``None`` to disable pagination.

---

### ``PERSONA_MANAGER_API_EXTRA_PERMISSION_CLASS``

**Type**: ``Optional[str]``

**Default**: ``None``

**Description**: Optionally specifies an additional permission class to extend the base permission (``IsAuthenticated``) for the API. This allows for more fine-grained access control, enabling you to restrict API access to users with a specific permission, in addition to requiring authentication.

---

### ``PERSONA_MANAGER_API_PARSER_CLASSES``

**Type**: ``List[str]``

**Default**:

```python
PERSONA_MANAGER_API_PARSER_CLASSES = [
   "rest_framework.parsers.JSONParser",
   "rest_framework.parsers.MultiPartParser",
   "rest_framework.parsers.FormParser",
]
```

**Description**: Specifies the parsers used to handle API request data formats. You can modify this list to add your parsers or set ``None`` if no parser needed.

---


### ``PERSONA_MANAGER_API_ORDERING_FIELDS``

**Type**: ``List[str]``

**Default**: ``["id", "persona_name", "created_at", "updated_at",]``

**Description**: Specifies the fields available for ordering in API queries, allowing the API responses to be sorted by these fields. you can see all available fields here

---

### ``PERSONA_MANAGER_API_SEARCH_FIELDS``

**Type**: ``List[str]``

**Default**: ``["persona_name", "description"]``

**Description**: Specifies the fields that are searchable in the API, allowing users to filter results based on these fields.

---

### All Available Fields

These are all fields that are available for searching, ordering, and filtering in the user personas:

- `id`: Unique identifier of the user persona (orderable, filterable).
- `persona_name`: The name of the user persona (searchable, filterable).
- `description`: A detailed description of the user persona (searchable).
- `is_active`: Indicates whether the user persona is active (filterable).
- `created_at`: The time when the user persona was created (orderable, filterable).
- `updated_at`: The time when the user persona was last updated (orderable, filterable).
- `attributes`: Additional attributes specific to the user persona (filterable).
- `image`: An image representing the user persona (filterable).

----

# Conclusion

We hope this documentation has provided a comprehensive guide to using and understanding the `dj-userpersona-manager`.

### Final Notes:
- **Version Compatibility**: Ensure your project meets the compatibility requirements for both Django and Python versions.
- **API Integration**: The package is designed for flexibility, allowing you to customize many features based on your application's needs.
- **Contributions**: Contributions are welcome! Feel free to check out the [Contributing guide](CONTRIBUTING.md) for more details.

If you encounter any issues or have feedback, please reach out via our [GitHub Issues page](https://github.com/lazarus-org/dj-userpersona-manager/issues).
