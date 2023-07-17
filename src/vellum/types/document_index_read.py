# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .document_index_status import DocumentIndexStatus
from .environment_enum import EnvironmentEnum


class DocumentIndexRead(pydantic.BaseModel):
    id: str
    created: str
    label: str = pydantic.Field(
        description=(
            'A human-readable label for the document index <span style="white-space: nowrap">`<= 150 characters`</span> \n'
        )
    )
    name: str = pydantic.Field(
        description=(
            'A name that uniquely identifies this index within its workspace <span style="white-space: nowrap">`<= 150 characters`</span> \n'
        )
    )
    status: typing.Optional[DocumentIndexStatus] = pydantic.Field(
        description=(
            "The current status of the document index\n" "\n" "* `ACTIVE` - Active\n" "* `ARCHIVED` - Archived\n"
        )
    )
    environment: typing.Optional[EnvironmentEnum] = pydantic.Field(
        description=(
            "The environment this document index is used in\n"
            "\n"
            "* `DEVELOPMENT` - Development\n"
            "* `STAGING` - Staging\n"
            "* `PRODUCTION` - Production\n"
        )
    )
    indexing_config: typing.Dict[str, typing.Any] = pydantic.Field(
        description=("Configuration representing how documents should be indexed\n")
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
