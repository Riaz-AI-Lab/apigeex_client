from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_request_type_0 import SearchRequestType0
from ...types import Response


def _get_kwargs(
    *,
    body: Union["SearchRequestType0", None],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1alpha/projects/lpr_healthcare/locations/us/collections/default_collection/dataStores/lpr_healthcare/servingConfigs/default_search:search",
    }

    _kwargs["json"]: Union[None, dict[str, Any]]
    if isinstance(body, SearchRequestType0):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
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
    body: Union["SearchRequestType0", None],
) -> Response[Any]:
    """Search Longitudinal Patient Record Content

     This API is a wrapper to the Google [search](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) API. Refer to
    this API for inputs/parameters.

    Args:
        body (Union['SearchRequestType0', None]): Refer to the
            [search](https://cloud.google.com/generative-ai-app-
            builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) api
            reference for supported attributes Example: {'query': 'Some example query', 'pageSize':
            10, 'queryExpansionSpec': {'condition': 'AUTO'}, 'spellCorrectionSpec': {'mode': 'AUTO'},
            'contentSearchSpec': {'summarySpec': {'summaryResultCount': 5, 'ignoreAdversarialQuery':
            True, 'includeCitations': True}, 'snippetSpec': {'returnSnippet': True},
            'extractiveContentSpec': {'maxExtractiveAnswerCount': 1}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union["SearchRequestType0", None],
) -> Response[Any]:
    """Search Longitudinal Patient Record Content

     This API is a wrapper to the Google [search](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) API. Refer to
    this API for inputs/parameters.

    Args:
        body (Union['SearchRequestType0', None]): Refer to the
            [search](https://cloud.google.com/generative-ai-app-
            builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) api
            reference for supported attributes Example: {'query': 'Some example query', 'pageSize':
            10, 'queryExpansionSpec': {'condition': 'AUTO'}, 'spellCorrectionSpec': {'mode': 'AUTO'},
            'contentSearchSpec': {'summarySpec': {'summaryResultCount': 5, 'ignoreAdversarialQuery':
            True, 'includeCitations': True}, 'snippetSpec': {'returnSnippet': True},
            'extractiveContentSpec': {'maxExtractiveAnswerCount': 1}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
