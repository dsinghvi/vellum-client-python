# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import pydantic_v1
from .named_test_case_variable_value_request import NamedTestCaseVariableValueRequest


class UpsertTestSuiteTestCaseRequest(pydantic_v1.BaseModel):
    id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The Vellum-generated ID of an existing Test Case whose data you'd like to replace. If specified and no Test Case exists with this ID, a 404 will be returned.
    """

    external_id: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    An ID external to Vellum that uniquely identifies the Test Case that you'd like to create/update. If there's a match on a Test Case that was previously created with the same external_id, it will be updated. Otherwise, a new Test Case will be created with this value as its external_id. If no external_id is specified, then a new Test Case will always be created.
    """

    label: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A human-readable label used to convey the intention of this Test Case
    """

    input_values: typing.List[NamedTestCaseVariableValueRequest] = pydantic_v1.Field()
    """
    Values for each of the Test Case's input variables
    """

    evaluation_values: typing.List[NamedTestCaseVariableValueRequest] = pydantic_v1.Field()
    """
    Values for each of the Test Case's evaluation variables
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
