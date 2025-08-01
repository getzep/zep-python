# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.entity_edge import EntityEdge
from ...types.entity_node import EntityNode
from ...types.episode_response import EpisodeResponse
from .raw_client import AsyncRawNodeClient, RawNodeClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class NodeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodeClient
        """
        return self._raw_client

    def get_by_graph_id(
        self,
        graph_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        uuid_cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityNode]:
        """
        Returns all nodes for a graph.

        Parameters
        ----------
        graph_id : str
            Graph ID

        limit : typing.Optional[int]
            Maximum number of items to return

        uuid_cursor : typing.Optional[str]
            UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityNode]
            Nodes

        Examples
        --------
        from zep_cloud import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.node.get_by_graph_id(
            graph_id="graph_id",
        )
        """
        _response = self._raw_client.get_by_graph_id(
            graph_id, limit=limit, uuid_cursor=uuid_cursor, request_options=request_options
        )
        return _response.data

    def get_by_user_id(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        uuid_cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityNode]:
        """
        Returns all nodes for a user

        Parameters
        ----------
        user_id : str
            User ID

        limit : typing.Optional[int]
            Maximum number of items to return

        uuid_cursor : typing.Optional[str]
            UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityNode]
            Nodes

        Examples
        --------
        from zep_cloud import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.node.get_by_user_id(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_by_user_id(
            user_id, limit=limit, uuid_cursor=uuid_cursor, request_options=request_options
        )
        return _response.data

    def get_edges(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a node

        Parameters
        ----------
        node_uuid : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        from zep_cloud import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.node.get_edges(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.get_edges(node_uuid, request_options=request_options)
        return _response.data

    def get_episodes(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EpisodeResponse:
        """
        Returns all episodes that mentioned a given node

        Parameters
        ----------
        node_uuid : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        from zep_cloud import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.node.get_episodes(
            node_uuid="node_uuid",
        )
        """
        _response = self._raw_client.get_episodes(node_uuid, request_options=request_options)
        return _response.data

    def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> EntityNode:
        """
        Returns a specific node by its UUID.

        Parameters
        ----------
        uuid_ : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityNode
            Node

        Examples
        --------
        from zep_cloud import Zep

        client = Zep(
            api_key="YOUR_API_KEY",
        )
        client.graph.node.get(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get(uuid_, request_options=request_options)
        return _response.data


class AsyncNodeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodeClient
        """
        return self._raw_client

    async def get_by_graph_id(
        self,
        graph_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        uuid_cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityNode]:
        """
        Returns all nodes for a graph.

        Parameters
        ----------
        graph_id : str
            Graph ID

        limit : typing.Optional[int]
            Maximum number of items to return

        uuid_cursor : typing.Optional[str]
            UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityNode]
            Nodes

        Examples
        --------
        import asyncio

        from zep_cloud import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.node.get_by_graph_id(
                graph_id="graph_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_graph_id(
            graph_id, limit=limit, uuid_cursor=uuid_cursor, request_options=request_options
        )
        return _response.data

    async def get_by_user_id(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = OMIT,
        uuid_cursor: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[EntityNode]:
        """
        Returns all nodes for a user

        Parameters
        ----------
        user_id : str
            User ID

        limit : typing.Optional[int]
            Maximum number of items to return

        uuid_cursor : typing.Optional[str]
            UUID based cursor, used for pagination. Should be the UUID of the last item in the previous page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityNode]
            Nodes

        Examples
        --------
        import asyncio

        from zep_cloud import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.node.get_by_user_id(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_by_user_id(
            user_id, limit=limit, uuid_cursor=uuid_cursor, request_options=request_options
        )
        return _response.data

    async def get_edges(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[EntityEdge]:
        """
        Returns all edges for a node

        Parameters
        ----------
        node_uuid : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[EntityEdge]
            Edges

        Examples
        --------
        import asyncio

        from zep_cloud import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.node.get_edges(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_edges(node_uuid, request_options=request_options)
        return _response.data

    async def get_episodes(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EpisodeResponse:
        """
        Returns all episodes that mentioned a given node

        Parameters
        ----------
        node_uuid : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeResponse
            Episodes

        Examples
        --------
        import asyncio

        from zep_cloud import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.node.get_episodes(
                node_uuid="node_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episodes(node_uuid, request_options=request_options)
        return _response.data

    async def get(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> EntityNode:
        """
        Returns a specific node by its UUID.

        Parameters
        ----------
        uuid_ : str
            Node UUID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntityNode
            Node

        Examples
        --------
        import asyncio

        from zep_cloud import AsyncZep

        client = AsyncZep(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.graph.node.get(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(uuid_, request_options=request_options)
        return _response.data
