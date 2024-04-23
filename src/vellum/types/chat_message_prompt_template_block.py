# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .prompt_template_block_state import PromptTemplateBlockState

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ChatMessagePromptTemplateBlock(pydantic.BaseModel):
    """
    A block of that represents a chat message in a prompt template.
    """

    properties: ChatMessagePromptTemplateBlockProperties
    id: str
    state: typing.Optional[PromptTemplateBlockState] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


from .chat_message_prompt_template_block_properties import ChatMessagePromptTemplateBlockProperties  # noqa: E402

ChatMessagePromptTemplateBlock.update_forward_refs()
