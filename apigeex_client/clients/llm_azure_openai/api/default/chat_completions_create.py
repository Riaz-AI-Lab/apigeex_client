from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_chat_completion_request import CreateChatCompletionRequest
from ...models.create_chat_completion_response import CreateChatCompletionResponse
from ...types import UNSET, Response


def _get_kwargs(
    deployment_id: str,
    *,
    body: CreateChatCompletionRequest,
    api_version: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["api-version"] = api_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/deployments/{deployment_id}/chat/completions",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateChatCompletionResponse]:
    if response.status_code == 200:
        response_200 = CreateChatCompletionResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateChatCompletionResponse]:
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
    body: CreateChatCompletionRequest,
    api_version: str,
) -> Response[CreateChatCompletionResponse]:
    """Creates a completion for the chat message

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (CreateChatCompletionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChatCompletionResponse]
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
    body: CreateChatCompletionRequest,
    api_version: str,
) -> Optional[CreateChatCompletionResponse]:
    """Creates a completion for the chat message

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (CreateChatCompletionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChatCompletionResponse
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
    body: CreateChatCompletionRequest,
    api_version: str,
) -> Response[CreateChatCompletionResponse]:
    """Creates a completion for the chat message

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (CreateChatCompletionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateChatCompletionResponse]
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
    body: CreateChatCompletionRequest,
    api_version: str,
) -> Optional[CreateChatCompletionResponse]:
    """Creates a completion for the chat message

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (CreateChatCompletionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateChatCompletionResponse
    """

    return (
        await asyncio_detailed(
            deployment_id=deployment_id,
            client=client,
            body=body,
            api_version=api_version,
        )
    ).parsed
