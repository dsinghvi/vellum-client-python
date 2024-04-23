# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .scenario_input_chat_history_variable_value import ScenarioInputChatHistoryVariableValue
from .scenario_input_string_variable_value import ScenarioInputStringVariableValue


class ScenarioInput_String(ScenarioInputStringVariableValue):
    type: typing.Literal["STRING"] = "STRING"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ScenarioInput_ChatHistory(ScenarioInputChatHistoryVariableValue):
    type: typing.Literal["CHAT_HISTORY"] = "CHAT_HISTORY"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ScenarioInput = typing.Union[ScenarioInput_String, ScenarioInput_ChatHistory]
