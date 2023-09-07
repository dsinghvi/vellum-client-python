# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime


class WorkflowExecutionActualJsonRequest(pydantic.BaseModel):
    output_id: typing.Optional[str] = pydantic.Field(
        description="The Vellum-generated ID of a workflow output. Must provide either this or output_key. output_key is typically preferred."
    )
    output_key: typing.Optional[str] = pydantic.Field(
        description="The user-defined name of a workflow output. Must provide either this or output_id. Should correspond to the `Name` specified in a Final Output Node. Generally preferred over output_id."
    )
    quality: typing.Optional[float] = pydantic.Field(
        description="Optionally provide a decimal number between 0.0 and 1.0 (inclusive) representing the quality of the output. 0 is the worst, 1 is the best."
    )
    timestamp: typing.Optional[float] = pydantic.Field(
        description="Optionally provide the timestamp representing when this feedback was collected. Used for reporting purposes."
    )
    desired_output_value: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        description="Optionally provide the value that the output ideally should have been."
    )

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
