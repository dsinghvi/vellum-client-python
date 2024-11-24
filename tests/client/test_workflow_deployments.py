# This file was auto-generated by Fern from our API Definition.

from vellum import Vellum
from vellum import AsyncVellum
import typing
from .utilities import validate_response


async def test_list_(client: Vellum, async_client: AsyncVellum) -> None:
    expected_response: typing.Any = {
        "count": 123,
        "next": "http://api.example.org/accounts/?offset=400&limit=100",
        "previous": "http://api.example.org/accounts/?offset=200&limit=100",
        "results": [
            {
                "id": "id",
                "name": "name",
                "label": "label",
                "status": "ACTIVE",
                "environment": "DEVELOPMENT",
                "created": "2024-01-15T09:30:00Z",
                "last_deployed_on": "2024-01-15T09:30:00Z",
                "input_variables": [{"id": "id", "key": "key", "type": "STRING"}],
                "output_variables": [{"id": "id", "key": "key", "type": "STRING"}],
                "description": "description",
            }
        ],
    }
    expected_types: typing.Any = {
        "count": "integer",
        "next": None,
        "previous": None,
        "results": (
            "list",
            {
                0: {
                    "id": None,
                    "name": None,
                    "label": None,
                    "status": None,
                    "environment": None,
                    "created": "datetime",
                    "last_deployed_on": "datetime",
                    "input_variables": ("list", {0: {"id": None, "key": None, "type": None}}),
                    "output_variables": ("list", {0: {"id": None, "key": None, "type": None}}),
                    "description": None,
                }
            },
        ),
    }
    response = client.workflow_deployments.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.workflow_deployments.list()
    validate_response(async_response, expected_response, expected_types)


async def test_retrieve(client: Vellum, async_client: AsyncVellum) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "label": "label",
        "status": "ACTIVE",
        "environment": "DEVELOPMENT",
        "created": "2024-01-15T09:30:00Z",
        "last_deployed_on": "2024-01-15T09:30:00Z",
        "last_deployed_history_item_id": "last_deployed_history_item_id",
        "input_variables": [
            {"id": "id", "key": "key", "type": "STRING", "required": True, "default": {"type": "STRING"}}
        ],
        "output_variables": [
            {"id": "id", "key": "key", "type": "STRING", "required": True, "default": {"type": "STRING"}}
        ],
        "description": "description",
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "label": None,
        "status": None,
        "environment": None,
        "created": "datetime",
        "last_deployed_on": "datetime",
        "last_deployed_history_item_id": None,
        "input_variables": (
            "list",
            {0: {"id": None, "key": None, "type": None, "required": None, "default": {"type": None}}},
        ),
        "output_variables": (
            "list",
            {0: {"id": None, "key": None, "type": None, "required": None, "default": {"type": None}}},
        ),
        "description": None,
    }
    response = client.workflow_deployments.retrieve(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.workflow_deployments.retrieve(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_list_workflow_release_tags(client: Vellum, async_client: AsyncVellum) -> None:
    expected_response: typing.Any = {
        "count": 123,
        "next": "http://api.example.org/accounts/?offset=400&limit=100",
        "previous": "http://api.example.org/accounts/?offset=200&limit=100",
        "results": [
            {"name": "name", "source": "SYSTEM", "history_item": {"id": "id", "timestamp": "2024-01-15T09:30:00Z"}}
        ],
    }
    expected_types: typing.Any = {
        "count": "integer",
        "next": None,
        "previous": None,
        "results": ("list", {0: {"name": None, "source": None, "history_item": {"id": None, "timestamp": "datetime"}}}),
    }
    response = client.workflow_deployments.list_workflow_release_tags(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.workflow_deployments.list_workflow_release_tags(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_retrieve_workflow_release_tag(client: Vellum, async_client: AsyncVellum) -> None:
    expected_response: typing.Any = {
        "name": "name",
        "source": "SYSTEM",
        "history_item": {"id": "id", "timestamp": "2024-01-15T09:30:00Z"},
    }
    expected_types: typing.Any = {"name": None, "source": None, "history_item": {"id": None, "timestamp": "datetime"}}
    response = client.workflow_deployments.retrieve_workflow_release_tag(id="id", name="name")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.workflow_deployments.retrieve_workflow_release_tag(id="id", name="name")
    validate_response(async_response, expected_response, expected_types)


async def test_update_workflow_release_tag(client: Vellum, async_client: AsyncVellum) -> None:
    expected_response: typing.Any = {
        "name": "name",
        "source": "SYSTEM",
        "history_item": {"id": "id", "timestamp": "2024-01-15T09:30:00Z"},
    }
    expected_types: typing.Any = {"name": None, "source": None, "history_item": {"id": None, "timestamp": "datetime"}}
    response = client.workflow_deployments.update_workflow_release_tag(id="id", name="name")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.workflow_deployments.update_workflow_release_tag(id="id", name="name")
    validate_response(async_response, expected_response, expected_types)