# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DeploymentReadStatusEnum(str, enum.Enum):
    """
    * `ACTIVE` - Active
    * `INACTIVE` - Inactive
    * `ARCHIVED` - Archived
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ARCHIVED = "ARCHIVED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        archived: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeploymentReadStatusEnum.ACTIVE:
            return active()
        if self is DeploymentReadStatusEnum.INACTIVE:
            return inactive()
        if self is DeploymentReadStatusEnum.ARCHIVED:
            return archived()
