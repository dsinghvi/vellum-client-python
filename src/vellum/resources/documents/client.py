# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...types.document_read import DocumentRead
from ...types.document_status import DocumentStatus
from ...types.paginated_slim_document_list import PaginatedSlimDocumentList
from ...types.upload_document_response import UploadDocumentResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        document_index_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        ordering: typing.Optional[str] = None,
    ) -> PaginatedSlimDocumentList:
        """
        Used to list documents. Optionally filter on supported fields.

        Parameters:
            - document_index_id: typing.Optional[str]. Filter down to only those documents that are included in the specified index. You may provide either the Vellum-generated ID or the unique name of the index specified upon initial creation.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - ordering: typing.Optional[str]. Which field to use when ordering the results.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", "v1/documents"),
            params=remove_none_from_dict(
                {"document_index_id": document_index_id, "limit": limit, "offset": offset, "ordering": ordering}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedSlimDocumentList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        label: typing.Optional[str] = OMIT,
        status: typing.Optional[DocumentStatus] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> DocumentRead:
        """
        Update a Document, keying off of its Vellum-generated ID. Particularly useful for updating its metadata.

        Parameters:
            - id: str. A UUID string identifying this document.

            - label: typing.Optional[str]. A human-readable label for the document. Defaults to the originally uploaded file's file name.

            - status: typing.Optional[DocumentStatus]. The current status of the document

                                                       * `ACTIVE` - Active
            - metadata: typing.Optional[typing.Dict[str, typing.Any]]. A JSON object containing any metadata associated with the document that you'd like to filter upon later.
        """
        _request: typing.Dict[str, typing.Any] = {}
        if label is not OMIT:
            _request["label"] = label
        if status is not OMIT:
            _request["status"] = status
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/documents/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def destroy(self, id: str) -> None:
        """
        Parameters:
            - id: str. A UUID string identifying this document.
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/documents/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def upload(
        self,
        *,
        add_to_index_names: typing.Optional[typing.List[str]] = None,
        external_id: typing.Optional[str] = None,
        label: str,
        contents: typing.IO,
        keywords: typing.Optional[typing.List[str]] = None,
        metadata: typing.Optional[str] = None,
    ) -> UploadDocumentResponse:
        """
        Upload a document to be indexed and used for search.

        **Note:** Uses a base url of `https://documents.vellum.ai`.

        Parameters:
            - add_to_index_names: typing.Optional[typing.List[str]].

            - external_id: typing.Optional[str].

            - label: str.

            - contents: typing.IO.

            - keywords: typing.Optional[typing.List[str]].

            - metadata: typing.Optional[str].
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().documents}/", "v1/upload-document"),
            data=jsonable_encoder(
                {
                    "add_to_index_names": add_to_index_names,
                    "external_id": external_id,
                    "label": label,
                    "keywords": keywords,
                    "metadata": metadata,
                }
            ),
            files={"contents": contents},
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UploadDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        document_index_id: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        ordering: typing.Optional[str] = None,
    ) -> PaginatedSlimDocumentList:
        """
        Used to list documents. Optionally filter on supported fields.

        Parameters:
            - document_index_id: typing.Optional[str]. Filter down to only those documents that are included in the specified index. You may provide either the Vellum-generated ID or the unique name of the index specified upon initial creation.

            - limit: typing.Optional[int]. Number of results to return per page.

            - offset: typing.Optional[int]. The initial index from which to return the results.

            - ordering: typing.Optional[str]. Which field to use when ordering the results.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", "v1/documents"),
            params=remove_none_from_dict(
                {"document_index_id": document_index_id, "limit": limit, "offset": offset, "ordering": ordering}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaginatedSlimDocumentList, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        label: typing.Optional[str] = OMIT,
        status: typing.Optional[DocumentStatus] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
    ) -> DocumentRead:
        """
        Update a Document, keying off of its Vellum-generated ID. Particularly useful for updating its metadata.

        Parameters:
            - id: str. A UUID string identifying this document.

            - label: typing.Optional[str]. A human-readable label for the document. Defaults to the originally uploaded file's file name.

            - status: typing.Optional[DocumentStatus]. The current status of the document

                                                       * `ACTIVE` - Active
            - metadata: typing.Optional[typing.Dict[str, typing.Any]]. A JSON object containing any metadata associated with the document that you'd like to filter upon later.
        """
        _request: typing.Dict[str, typing.Any] = {}
        if label is not OMIT:
            _request["label"] = label
        if status is not OMIT:
            _request["status"] = status
        if metadata is not OMIT:
            _request["metadata"] = metadata
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/documents/{id}"),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DocumentRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def destroy(self, id: str) -> None:
        """
        Parameters:
            - id: str. A UUID string identifying this document.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/documents/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def upload(
        self,
        *,
        add_to_index_names: typing.Optional[typing.List[str]] = None,
        external_id: typing.Optional[str] = None,
        label: str,
        contents: typing.IO,
        keywords: typing.Optional[typing.List[str]] = None,
        metadata: typing.Optional[str] = None,
    ) -> UploadDocumentResponse:
        """
        Upload a document to be indexed and used for search.

        **Note:** Uses a base url of `https://documents.vellum.ai`.

        Parameters:
            - add_to_index_names: typing.Optional[typing.List[str]].

            - external_id: typing.Optional[str].

            - label: str.

            - contents: typing.IO.

            - keywords: typing.Optional[typing.List[str]].

            - metadata: typing.Optional[str].
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().documents}/", "v1/upload-document"),
            data=jsonable_encoder(
                {
                    "add_to_index_names": add_to_index_names,
                    "external_id": external_id,
                    "label": label,
                    "keywords": keywords,
                    "metadata": metadata,
                }
            ),
            files={"contents": contents},
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(UploadDocumentResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
