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
from ...types.api_error import ApiError as types_api_error_ApiError
from ...types.episode import Episode
from ...types.episode_response import EpisodeResponse


class EpisodeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_by_group_id(
        self,
        group_id: str,
        *,
        lastn: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeResponse:
        """
        Get episodes by Group ID

        Parameters
        ----------
        group_id : str
            Group ID

        lastn : typing.Optional[int]
            The number of most recent episodes to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.episode.get_by_group_id(
            group_id="group_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/episodes/group/{jsonable_encoder(group_id)}",
            method="GET",
            params={"lastn": lastn},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EpisodeResponse, _response.json())  # type: ignore
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
        lastn: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeResponse:
        """
        Get episodes by User ID

        Parameters
        ----------
        user_id : str
            User ID

        lastn : typing.Optional[int]
            The number of most recent episodes entries to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.episode.get_by_user_id(
            user_id="user_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/episodes/user/{jsonable_encoder(user_id)}",
            method="GET",
            params={"lastn": lastn},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EpisodeResponse, _response.json())  # type: ignore
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

    def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> Episode:
        """
        Get episode by UUID

        Parameters
        ----------
        uuid_ : str
            Episode UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Episode
            Episode

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.episode.get(
            uuid_="uuid",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"graph/episodes/{jsonable_encoder(uuid_)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Episode, _response.json())  # type: ignore
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


class AsyncEpisodeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_by_group_id(
        self,
        group_id: str,
        *,
        lastn: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeResponse:
        """
        Get episodes by Group ID

        Parameters
        ----------
        group_id : str
            Group ID

        lastn : typing.Optional[int]
            The number of most recent episodes to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.episode.get_by_group_id(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/episodes/group/{jsonable_encoder(group_id)}",
            method="GET",
            params={"lastn": lastn},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EpisodeResponse, _response.json())  # type: ignore
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
        lastn: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EpisodeResponse:
        """
        Get episodes by User ID

        Parameters
        ----------
        user_id : str
            User ID

        lastn : typing.Optional[int]
            The number of most recent episodes entries to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.episode.get_by_user_id(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/episodes/user/{jsonable_encoder(user_id)}",
            method="GET",
            params={"lastn": lastn},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EpisodeResponse, _response.json())  # type: ignore
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

    async def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> Episode:
        """
        Get episode by UUID

        Parameters
        ----------
        uuid_ : str
            Episode UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Episode
            Episode

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.episode.get(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"graph/episodes/{jsonable_encoder(uuid_)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Episode, _response.json())  # type: ignore
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
