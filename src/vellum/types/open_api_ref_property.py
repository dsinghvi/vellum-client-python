# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OpenApiRefProperty(UniversalBaseModel):
    """
    An OpenAPI specification of a property that is a URI-reference to another schema
    """

    type: typing.Literal["ref"] = "ref"
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    ref: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow