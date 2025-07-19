from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.extensions_chat_completions_request import ExtensionsChatCompletionsRequest
from ...models.extensions_chat_completions_response import ExtensionsChatCompletionsResponse
from ...types import UNSET, Response


def _get_kwargs(
    deployment_id: str,
    *,
    body: ExtensionsChatCompletionsRequest,
    api_version: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["api-version"] = api_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/deployments/{deployment_id}/extensions/chat/completions",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExtensionsChatCompletionsResponse]:
    if response.status_code == 200:
        response_200 = ExtensionsChatCompletionsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExtensionsChatCompletionsResponse]:
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
    body: ExtensionsChatCompletionsRequest,
    api_version: str,
) -> Response[ExtensionsChatCompletionsResponse]:
    r"""Using extensions to creates a completion for the chat messages.

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (ExtensionsChatCompletionsRequest): Request for the chat completions using extensions
            Example: {'dataSources': [{'type': 'AzureCognitiveSearch', 'parameters': {'endpoint':
            'https://mysearchexample.search.windows.net', 'key': '***(admin key)', 'indexName': 'my-
            chunk-index', 'fieldsMapping': {'titleField': 'productName', 'urlField': 'productUrl',
            'filepathField': 'productFilePath', 'contentFields': ['productDescription'],
            'contentFieldsSeparator': '\n'}, 'topNDocuments': 5, 'queryType': 'semantic',
            'semanticConfiguration': 'defaultConfiguration', 'inScope': True, 'roleInformation':
            'roleInformation'}}], 'messages': [{'role': 'user', 'content': 'Where can I find a hiking
            place in Seattle?'}], 'temperature': 0.9}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionsChatCompletionsResponse]
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
    body: ExtensionsChatCompletionsRequest,
    api_version: str,
) -> Optional[ExtensionsChatCompletionsResponse]:
    r"""Using extensions to creates a completion for the chat messages.

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (ExtensionsChatCompletionsRequest): Request for the chat completions using extensions
            Example: {'dataSources': [{'type': 'AzureCognitiveSearch', 'parameters': {'endpoint':
            'https://mysearchexample.search.windows.net', 'key': '***(admin key)', 'indexName': 'my-
            chunk-index', 'fieldsMapping': {'titleField': 'productName', 'urlField': 'productUrl',
            'filepathField': 'productFilePath', 'contentFields': ['productDescription'],
            'contentFieldsSeparator': '\n'}, 'topNDocuments': 5, 'queryType': 'semantic',
            'semanticConfiguration': 'defaultConfiguration', 'inScope': True, 'roleInformation':
            'roleInformation'}}], 'messages': [{'role': 'user', 'content': 'Where can I find a hiking
            place in Seattle?'}], 'temperature': 0.9}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionsChatCompletionsResponse
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
    body: ExtensionsChatCompletionsRequest,
    api_version: str,
) -> Response[ExtensionsChatCompletionsResponse]:
    r"""Using extensions to creates a completion for the chat messages.

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (ExtensionsChatCompletionsRequest): Request for the chat completions using extensions
            Example: {'dataSources': [{'type': 'AzureCognitiveSearch', 'parameters': {'endpoint':
            'https://mysearchexample.search.windows.net', 'key': '***(admin key)', 'indexName': 'my-
            chunk-index', 'fieldsMapping': {'titleField': 'productName', 'urlField': 'productUrl',
            'filepathField': 'productFilePath', 'contentFields': ['productDescription'],
            'contentFieldsSeparator': '\n'}, 'topNDocuments': 5, 'queryType': 'semantic',
            'semanticConfiguration': 'defaultConfiguration', 'inScope': True, 'roleInformation':
            'roleInformation'}}], 'messages': [{'role': 'user', 'content': 'Where can I find a hiking
            place in Seattle?'}], 'temperature': 0.9}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExtensionsChatCompletionsResponse]
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
    body: ExtensionsChatCompletionsRequest,
    api_version: str,
) -> Optional[ExtensionsChatCompletionsResponse]:
    r"""Using extensions to creates a completion for the chat messages.

    Args:
        deployment_id (str): Deployment id of the model which was deployed.
        api_version (str): api version Example: 2023-08-01-preview.
        body (ExtensionsChatCompletionsRequest): Request for the chat completions using extensions
            Example: {'dataSources': [{'type': 'AzureCognitiveSearch', 'parameters': {'endpoint':
            'https://mysearchexample.search.windows.net', 'key': '***(admin key)', 'indexName': 'my-
            chunk-index', 'fieldsMapping': {'titleField': 'productName', 'urlField': 'productUrl',
            'filepathField': 'productFilePath', 'contentFields': ['productDescription'],
            'contentFieldsSeparator': '\n'}, 'topNDocuments': 5, 'queryType': 'semantic',
            'semanticConfiguration': 'defaultConfiguration', 'inScope': True, 'roleInformation':
            'roleInformation'}}], 'messages': [{'role': 'user', 'content': 'Where can I find a hiking
            place in Seattle?'}], 'temperature': 0.9}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExtensionsChatCompletionsResponse
    """

    return (
        await asyncio_detailed(
            deployment_id=deployment_id,
            client=client,
            body=body,
            api_version=api_version,
        )
    ).parsed
