# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .test_suite_test_case_create_bulk_operation_request import TestSuiteTestCaseCreateBulkOperationRequest
from .test_suite_test_case_delete_bulk_operation_request import TestSuiteTestCaseDeleteBulkOperationRequest
from .test_suite_test_case_replace_bulk_operation_request import TestSuiteTestCaseReplaceBulkOperationRequest
from .test_suite_test_case_upsert_bulk_operation_request import TestSuiteTestCaseUpsertBulkOperationRequest


class TestSuiteTestCaseBulkOperationRequest_Create(TestSuiteTestCaseCreateBulkOperationRequest):
    type: typing.Literal["CREATE"] = "CREATE"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class TestSuiteTestCaseBulkOperationRequest_Replace(TestSuiteTestCaseReplaceBulkOperationRequest):
    type: typing.Literal["REPLACE"] = "REPLACE"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class TestSuiteTestCaseBulkOperationRequest_Upsert(TestSuiteTestCaseUpsertBulkOperationRequest):
    type: typing.Literal["UPSERT"] = "UPSERT"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class TestSuiteTestCaseBulkOperationRequest_Delete(TestSuiteTestCaseDeleteBulkOperationRequest):
    type: typing.Literal["DELETE"] = "DELETE"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


TestSuiteTestCaseBulkOperationRequest = typing.Union[
    TestSuiteTestCaseBulkOperationRequest_Create,
    TestSuiteTestCaseBulkOperationRequest_Replace,
    TestSuiteTestCaseBulkOperationRequest_Upsert,
    TestSuiteTestCaseBulkOperationRequest_Delete,
]
