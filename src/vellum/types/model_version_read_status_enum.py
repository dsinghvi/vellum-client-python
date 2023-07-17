# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ModelVersionReadStatusEnum(str, enum.Enum):
    """
    * `CREATING` - Creating
    * `READY` - Ready
    * `CREATION_FAILED` - Creation Failed
    * `DISABLED` - Disabled
    """

    CREATING = "CREATING"
    READY = "READY"
    CREATION_FAILED = "CREATION_FAILED"
    DISABLED = "DISABLED"

    def visit(
        self,
        creating: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        creation_failed: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ModelVersionReadStatusEnum.CREATING:
            return creating()
        if self is ModelVersionReadStatusEnum.READY:
            return ready()
        if self is ModelVersionReadStatusEnum.CREATION_FAILED:
            return creation_failed()
        if self is ModelVersionReadStatusEnum.DISABLED:
            return disabled()
