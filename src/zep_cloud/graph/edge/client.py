# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError as core_api_error_ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...errors.bad_request_error import BadRequestError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.entity_edge import EntityEdge
from ...types.success_response import SuccessResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class EdgeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_by_group_id(
        self,
        group_id: str,
        *,
        created_at_cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a group.

        Parameters
        ----------
        group_id : str
            Group ID

        created_at_cursor : typing.Optional[str]
            Return only items created after this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.edge.get_by_group_id(
            group_id="group_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/edge/group/{jsonable_encoder(group_id)}",
            method="POST",
            json={"created_at_cursor": created_at_cursor, "limit": limit},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[EntityEdge], _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_user_id(
        self,
        user_id: str,
        *,
        created_at_cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a user.

        Parameters
        ----------
        user_id : str
            User ID

        created_at_cursor : typing.Optional[str]
            Return only items created after this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.edge.get_by_user_id(
            user_id="user_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/edge/user/{jsonable_encoder(user_id)}",
            method="POST",
            json={"created_at_cursor": created_at_cursor, "limit": limit},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[EntityEdge], _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> EntityEdge:
        """
        Returns a specific edge by its UUID.

        Parameters
        ----------
        uuid_ : str
            Edge UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityEdge
            Edge

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.edge.get(
            uuid_="uuid",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/edge/{jsonable_encoder(uuid_)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntityEdge, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Deletes an edge by UUID.

        Parameters
        ----------
        uuid_ : str
            Edge UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Edge deleted

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.edge.delete(
            uuid_="uuid",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/edge/{jsonable_encoder(uuid_)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEdgeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_by_group_id(
        self,
        group_id: str,
        *,
        created_at_cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a group.

        Parameters
        ----------
        group_id : str
            Group ID

        created_at_cursor : typing.Optional[str]
            Return only items created after this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.edge.get_by_group_id(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/edge/group/{jsonable_encoder(group_id)}",
            method="POST",
            json={"created_at_cursor": created_at_cursor, "limit": limit},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[EntityEdge], _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_user_id(
        self,
        user_id: str,
        *,
        created_at_cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a user.

        Parameters
        ----------
        user_id : str
            User ID

        created_at_cursor : typing.Optional[str]
            Return only items created after this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.edge.get_by_user_id(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/edge/user/{jsonable_encoder(user_id)}",
            method="POST",
            json={"created_at_cursor": created_at_cursor, "limit": limit},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(typing.List[EntityEdge], _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> EntityEdge:
        """
        Returns a specific edge by its UUID.

        Parameters
        ----------
        uuid_ : str
            Edge UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityEdge
            Edge

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.edge.get(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/edge/{jsonable_encoder(uuid_)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntityEdge, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Deletes an edge by UUID.

        Parameters
        ----------
        uuid_ : str
            Edge UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Edge deleted

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.edge.delete(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/edge/{jsonable_encoder(uuid_)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(types_api_error_ApiError, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(status_code=_response.status_code, body=_response.text)
        raise core_api_error_ApiError(status_code=_response.status_code, body=_response_json)
