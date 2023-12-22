# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .finish_reason_enum import FinishReasonEnum
from .normalized_log_probs import NormalizedLogProbs
from .vellum_variable_type import VellumVariableType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EnrichedNormalizedCompletion(pydantic.BaseModel):
    id: str = pydantic.Field(description="The Vellum-generated ID of the completion.")
    external_id: typing.Optional[str] = pydantic.Field(
        description="The external ID that was originally provided along with the generation request, which uniquely identifies this generation in an external system."
    )
    text: str = pydantic.Field(description="The text generated by the LLM.")
    finish_reason: typing.Optional[FinishReasonEnum] = pydantic.Field(
        description=(
            "The reason the generation finished.\n"
            "\n"
            "- `LENGTH` - LENGTH\n"
            "- `STOP` - STOP\n"
            "- `UNKNOWN` - UNKNOWN\n"
        )
    )
    logprobs: typing.Optional[NormalizedLogProbs] = pydantic.Field(
        description="The logprobs of the completion. Only present if specified in the original request options."
    )
    model_version_id: str = pydantic.Field(description="The ID of the model version used to generate this completion.")
    prompt_version_id: str
    type: typing.Optional[VellumVariableType]
    deployment_release_tag: str
    model_name: str

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
