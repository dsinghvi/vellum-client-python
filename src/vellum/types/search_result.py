# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ..core.datetime_utils import serialize_datetime
from .document import Document


class SearchResult(pydantic.BaseModel):
    document: Document = pydantic.Field(
        description=("The document that contains the chunk that matched the search query.\n")
    )
    text: str = pydantic.Field(description=("The text of the chunk that matched the search query.\n"))
    keywords: typing.List[str]
    score: float = pydantic.Field(description=("A score representing how well the chunk matches the search query.\n"))

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}