from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    query_model: Union[Unset, str] = UNSET,
    user_pseudo_id: Union[Unset, str] = UNSET,
    include_tail_suggestions: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["query"] = query

    params["queryModel"] = query_model

    params["userPseudoId"] = user_pseudo_id

    params["includeTailSuggestions"] = include_tail_suggestions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1alpha/projects/lpr_healthcare/locations/us/collections/default_collection/dataStores/lpr_healthcare:completeQuery",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 401:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    query_model: Union[Unset, str] = UNSET,
    user_pseudo_id: Union[Unset, str] = UNSET,
    include_tail_suggestions: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Completes the specified user input with keyword suggestions.

     This API is a wrapper to the Google [completeQuery](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) API. Refer to this API
    for inputs/parameters.

    Args:
        query (str):
        query_model (Union[Unset, str]):
        user_pseudo_id (Union[Unset, str]):
        include_tail_suggestions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        query=query,
        query_model=query_model,
        user_pseudo_id=user_pseudo_id,
        include_tail_suggestions=include_tail_suggestions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    query: str,
    query_model: Union[Unset, str] = UNSET,
    user_pseudo_id: Union[Unset, str] = UNSET,
    include_tail_suggestions: Union[Unset, bool] = UNSET,
) -> Response[Any]:
    """Completes the specified user input with keyword suggestions.

     This API is a wrapper to the Google [completeQuery](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) API. Refer to this API
    for inputs/parameters.

    Args:
        query (str):
        query_model (Union[Unset, str]):
        user_pseudo_id (Union[Unset, str]):
        include_tail_suggestions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        query=query,
        query_model=query_model,
        user_pseudo_id=user_pseudo_id,
        include_tail_suggestions=include_tail_suggestions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
