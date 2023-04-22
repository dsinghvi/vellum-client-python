# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ProviderEnum(str, enum.Enum):
    ANTHROPIC = "ANTHROPIC"
    COHERE = "COHERE"
    GOOGLE = "GOOGLE"
    HOSTED = "HOSTED"
    OPENAI = "OPENAI"
    PYQ = "PYQ"

    def visit(
        self,
        anthropic: typing.Callable[[], T_Result],
        cohere: typing.Callable[[], T_Result],
        google: typing.Callable[[], T_Result],
        hosted: typing.Callable[[], T_Result],
        openai: typing.Callable[[], T_Result],
        pyq: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderEnum.ANTHROPIC:
            return anthropic()
        if self is ProviderEnum.COHERE:
            return cohere()
        if self is ProviderEnum.GOOGLE:
            return google()
        if self is ProviderEnum.HOSTED:
            return hosted()
        if self is ProviderEnum.OPENAI:
            return openai()
        if self is ProviderEnum.PYQ:
            return pyq()
