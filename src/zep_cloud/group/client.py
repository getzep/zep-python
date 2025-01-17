# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.apidata_fact_rating_instruction import ApidataFactRatingInstruction
from ..types.apidata_group_list_response import ApidataGroupListResponse
from ..types.facts_response import FactsResponse
from ..types.group import Group
from ..types.success_response import SuccessResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class GroupClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add(
        self,
        *,
        group_id: str,
        description: typing.Optional[str] = OMIT,
        fact_rating_instruction: typing.Optional[ApidataFactRatingInstruction] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new user group

        Parameters
        ----------
        group_id : str

        description : typing.Optional[str]

        fact_rating_instruction : typing.Optional[ApidataFactRatingInstruction]
            UserIDs     []string `json:"user_ids"`

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            The added group

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.group.add(
            group_id="group_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            json={
                "description": description,
                "fact_rating_instruction": fact_rating_instruction,
                "group_id": group_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Group, _response.json())  # type: ignore
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

    def list_all_groups(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApidataGroupListResponse:
        """
        List all groups with pagination.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Page number for pagination, starting from 1

        page_size : typing.Optional[int]
            Number of groups to retrieve per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApidataGroupListResponse
            Successfully retrieved list of groups

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.group.list_all_groups()
        """
        _response = self._client_wrapper.httpx_client.request(
            "groups-ordered",
            method="GET",
            params={"pageNumber": page_number, "pageSize": page_size},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ApidataGroupListResponse, _response.json())  # type: ignore
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

    def get_a_group(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a group.

        Parameters
        ----------
        group_id : str
            The group_id of the group to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            The group that was retrieved.

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.group.get_a_group(
            group_id="groupId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Group, _response.json())  # type: ignore
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

    def delete(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SuccessResponse:
        """
        Delete group

        Parameters
        ----------
        group_id : str
            Group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Deleted

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.group.delete(
            group_id="groupId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
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

    def get_facts(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> FactsResponse:
        """
        Get group facts.

        Parameters
        ----------
        group_id : str
            The group_id of the group to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FactsResponse
            The group facts.

        Examples
        --------
        from zep_cloud.client import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.group.get_facts(
            group_id="groupId",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/facts", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(FactsResponse, _response.json())  # type: ignore
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


class AsyncGroupClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add(
        self,
        *,
        group_id: str,
        description: typing.Optional[str] = OMIT,
        fact_rating_instruction: typing.Optional[ApidataFactRatingInstruction] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Create a new user group

        Parameters
        ----------
        group_id : str

        description : typing.Optional[str]

        fact_rating_instruction : typing.Optional[ApidataFactRatingInstruction]
            UserIDs     []string `json:"user_ids"`

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            The added group

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.group.add(
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups",
            method="POST",
            json={
                "description": description,
                "fact_rating_instruction": fact_rating_instruction,
                "group_id": group_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Group, _response.json())  # type: ignore
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

    async def list_all_groups(
        self,
        *,
        page_number: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApidataGroupListResponse:
        """
        List all groups with pagination.

        Parameters
        ----------
        page_number : typing.Optional[int]
            Page number for pagination, starting from 1

        page_size : typing.Optional[int]
            Number of groups to retrieve per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApidataGroupListResponse
            Successfully retrieved list of groups

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.group.list_all_groups()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "groups-ordered",
            method="GET",
            params={"pageNumber": page_number, "pageSize": page_size},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ApidataGroupListResponse, _response.json())  # type: ignore
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

    async def get_a_group(self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Group:
        """
        Get a group.

        Parameters
        ----------
        group_id : str
            The group_id of the group to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            The group that was retrieved.

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.group.get_a_group(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(Group, _response.json())  # type: ignore
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

    async def delete(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SuccessResponse:
        """
        Delete group

        Parameters
        ----------
        group_id : str
            Group ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SuccessResponse
            Deleted

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.group.delete(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SuccessResponse, _response.json())  # type: ignore
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

    async def get_facts(
        self, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FactsResponse:
        """
        Get group facts.

        Parameters
        ----------
        group_id : str
            The group_id of the group to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FactsResponse
            The group facts.

        Examples
        --------
        import asyncio

        from zep_cloud.client import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.group.get_facts(
                group_id="groupId",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/facts", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(FactsResponse, _response.json())  # type: ignore
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
