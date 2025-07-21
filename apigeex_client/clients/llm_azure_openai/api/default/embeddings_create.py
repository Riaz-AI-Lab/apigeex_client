from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.embeddings_create_body import EmbeddingsCreateBody
from ...models.embeddings_create_response_200 import EmbeddingsCreateResponse200
from ...types import UNSET, Response


def _get_kwargs(
    deployment_id: str,
    *,
    body: EmbeddingsCreateBody,
    api_version: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["api-version"] = api_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/deployments/{deployment_id}/embeddings",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EmbeddingsCreateResponse200]:
    if response.status_code == 200:
        response_200 = EmbeddingsCreateResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EmbeddingsCreateResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmbeddingsCreateBody,
    api_version: str,
) -> Response[EmbeddingsCreateResponse200]:
    """Get a vector representation of a given input that can be easily consumed by machine learning models
    and algorithms.

    Args:
        deployment_id (str):  Example: ada-search-index-v1.
        api_version (str): api version Example: 2023-08-01-preview.
        body (EmbeddingsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingsCreateResponse200]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
        body=body,
        api_version=api_version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmbeddingsCreateBody,
    api_version: str,
) -> Optional[EmbeddingsCreateResponse200]:
    """Get a vector representation of a given input that can be easily consumed by machine learning models
    and algorithms.

    Args:
        deployment_id (str):  Example: ada-search-index-v1.
        api_version (str): api version Example: 2023-08-01-preview.
        body (EmbeddingsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingsCreateResponse200
    """

    return sync_detailed(
        deployment_id=deployment_id,
        client=client,
        body=body,
        api_version=api_version,
    ).parsed


async def asyncio_detailed(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmbeddingsCreateBody,
    api_version: str,
) -> Response[EmbeddingsCreateResponse200]:
    """Get a vector representation of a given input that can be easily consumed by machine learning models
    and algorithms.

    Args:
        deployment_id (str):  Example: ada-search-index-v1.
        api_version (str): api version Example: 2023-08-01-preview.
        body (EmbeddingsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmbeddingsCreateResponse200]
    """

    kwargs = _get_kwargs(
        deployment_id=deployment_id,
        body=body,
        api_version=api_version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    deployment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: EmbeddingsCreateBody,
    api_version: str,
) -> Optional[EmbeddingsCreateResponse200]:
    """Get a vector representation of a given input that can be easily consumed by machine learning models
    and algorithms.

    Args:
        deployment_id (str):  Example: ada-search-index-v1.
        api_version (str): api version Example: 2023-08-01-preview.
        body (EmbeddingsCreateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmbeddingsCreateResponse200
    """

    return (
        await asyncio_detailed(
            deployment_id=deployment_id,
            client=client,
            body=body,
            api_version=api_version,
        )
    ).parsed
