# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import VellumEnvironment
from ...types.document_index_read import DocumentIndexRead
from ...types.document_index_status import DocumentIndexStatus
from ...types.environment_enum import EnvironmentEnum

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentIndexesClient:
    def __init__(
        self, *, environment: VellumEnvironment = VellumEnvironment.PRODUCTION, client_wrapper: SyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def create(
        self,
        *,
        label: str,
        name: str,
        status: typing.Optional[DocumentIndexStatus] = OMIT,
        environment: typing.Optional[EnvironmentEnum] = OMIT,
        indexing_config: typing.Dict[str, typing.Any],
        copy_documents_from_index_id: typing.Optional[str] = OMIT,
    ) -> DocumentIndexRead:
        """
        <strong style="background-color:#ffc107; color:white; padding:4px; border-radius:4px">Unstable</strong>

        Creates a new document index.

        Parameters:
            - label: str. A human-readable label for the document index <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 150 characters`</span>

            - name: str. A name that uniquely identifies this index within its workspace <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 150 characters`</span>

            - status: typing.Optional[DocumentIndexStatus]. The current status of the document index

                                                            * `ACTIVE` - Active
                                                            * `ARCHIVED` - Archived
            - environment: typing.Optional[EnvironmentEnum]. The environment this document index is used in

                                                             * `DEVELOPMENT` - Development
                                                             * `STAGING` - Staging
                                                             * `PRODUCTION` - Production
            - indexing_config: typing.Dict[str, typing.Any]. Configuration representing how documents should be indexed

            - copy_documents_from_index_id: typing.Optional[str]. Optionally specify the id of a document index from which you'd like to copy and re-index its documents into this newly created index
        """
        _request: typing.Dict[str, typing.Any] = {"label": label, "name": name, "indexing_config": indexing_config}
        if status is not OMIT:
            _request["status"] = status
        if environment is not OMIT:
            _request["environment"] = environment
        if copy_documents_from_index_id is not OMIT:
            _request["copy_documents_from_index_id"] = copy_documents_from_index_id
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.default}/", "v1/document-indexes"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentIndexRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentIndexesClient:
    def __init__(
        self, *, environment: VellumEnvironment = VellumEnvironment.PRODUCTION, client_wrapper: AsyncClientWrapper
    ):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def create(
        self,
        *,
        label: str,
        name: str,
        status: typing.Optional[DocumentIndexStatus] = OMIT,
        environment: typing.Optional[EnvironmentEnum] = OMIT,
        indexing_config: typing.Dict[str, typing.Any],
        copy_documents_from_index_id: typing.Optional[str] = OMIT,
    ) -> DocumentIndexRead:
        """
        <strong style="background-color:#ffc107; color:white; padding:4px; border-radius:4px">Unstable</strong>

        Creates a new document index.

        Parameters:
            - label: str. A human-readable label for the document index <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 150 characters`</span>

            - name: str. A name that uniquely identifies this index within its workspace <span style="white-space: nowrap">`non-empty`</span> <span style="white-space: nowrap">`<= 150 characters`</span>

            - status: typing.Optional[DocumentIndexStatus]. The current status of the document index

                                                            * `ACTIVE` - Active
                                                            * `ARCHIVED` - Archived
            - environment: typing.Optional[EnvironmentEnum]. The environment this document index is used in

                                                             * `DEVELOPMENT` - Development
                                                             * `STAGING` - Staging
                                                             * `PRODUCTION` - Production
            - indexing_config: typing.Dict[str, typing.Any]. Configuration representing how documents should be indexed

            - copy_documents_from_index_id: typing.Optional[str]. Optionally specify the id of a document index from which you'd like to copy and re-index its documents into this newly created index
        """
        _request: typing.Dict[str, typing.Any] = {"label": label, "name": name, "indexing_config": indexing_config}
        if status is not OMIT:
            _request["status"] = status
        if environment is not OMIT:
            _request["environment"] = environment
        if copy_documents_from_index_id is not OMIT:
            _request["copy_documents_from_index_id"] = copy_documents_from_index_id
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.default}/", "v1/document-indexes"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentIndexRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
