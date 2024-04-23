# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .chat_history_prompt_template_block import ChatHistoryPromptTemplateBlock
from .chat_message_prompt_template_block_properties import ChatMessagePromptTemplateBlockProperties
from .function_definition_prompt_template_block import FunctionDefinitionPromptTemplateBlock
from .jinja_prompt_template_block import JinjaPromptTemplateBlock


class PromptTemplateBlock_Jinja(JinjaPromptTemplateBlock):
    block_type: typing.Literal["JINJA"] = "JINJA"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class PromptTemplateBlock_ChatHistory(ChatHistoryPromptTemplateBlock):
    block_type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class PromptTemplateBlock_ChatMessage(ChatMessagePromptTemplateBlock):
    block_type: typing.Literal["CHAT_MESSAGE"] = "CHAT_MESSAGE"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class PromptTemplateBlock_FunctionDefinition(FunctionDefinitionPromptTemplateBlock):
    block_type: typing.Literal["FUNCTION_DEFINITION"] = "FUNCTION_DEFINITION"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


PromptTemplateBlock = typing.Union[
    PromptTemplateBlock_Jinja,
    PromptTemplateBlock_ChatHistory,
    PromptTemplateBlock_ChatMessage,
    PromptTemplateBlock_FunctionDefinition,
]
from .chat_message_prompt_template_block import ChatMessagePromptTemplateBlock  # noqa: E402

PromptTemplateBlock_ChatMessage.update_forward_refs(
    ChatMessagePromptTemplateBlock=ChatMessagePromptTemplateBlock,
    ChatMessagePromptTemplateBlockProperties=ChatMessagePromptTemplateBlockProperties,
    PromptTemplateBlock=PromptTemplateBlock,
)
