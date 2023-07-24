# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .model_type_enum import ModelTypeEnum
from .model_version_build_config import ModelVersionBuildConfig
from .model_version_exec_config import ModelVersionExecConfig
from .model_version_read_status_enum import ModelVersionReadStatusEnum
from .provider_enum import ProviderEnum


class ModelVersionRead(pydantic.BaseModel):
    id: str = pydantic.Field(description="Vellum-generated ID that uniquely identifies this model version.")
    created: str = pydantic.Field(description="Timestamp of when this model version was created.")
    label: str = pydantic.Field(
        description='Human-friendly name for this model version. <span style="white-space: nowrap">`<= 150 characters`</span> '
    )
    model_type: ModelTypeEnum = pydantic.Field(
        description=(
            "The type of task this model is used for.\n" "\n" "* `GENERATE` - Generate\n" "* `CLASSIFY` - Classify\n"
        )
    )
    provider: ProviderEnum = pydantic.Field(
        description=(
            "Which LLM provider this model version is associated with.\n"
            "\n"
            "* `ANTHROPIC` - Anthropic\n"
            "* `COHERE` - Cohere\n"
            "* `GOOGLE` - Google\n"
            "* `HOSTED` - Hosted\n"
            "* `MOSAICML` - MosaicML\n"
            "* `MYSTIC` - Mystic\n"
            "* `OPENAI` - OpenAI\n"
            "* `PYQ` - Pyq\n"
        )
    )
    external_id: str = pydantic.Field(
        description='The unique id of this model version as it exists in the above provider\'s system. <span style="white-space: nowrap">`<= 250 characters`</span> '
    )
    build_config: ModelVersionBuildConfig = pydantic.Field(
        description="Configuration used to build this model version."
    )
    exec_config: ModelVersionExecConfig = pydantic.Field(
        description="Configuration used to execute this model version."
    )
    status: typing.Optional[ModelVersionReadStatusEnum]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
