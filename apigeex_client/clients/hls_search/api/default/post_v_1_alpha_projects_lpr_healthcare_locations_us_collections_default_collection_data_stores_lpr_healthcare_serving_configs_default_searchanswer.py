from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.answer_request_type_0 import AnswerRequestType0
from ...types import Response


def _get_kwargs(
    *,
    body: Union["AnswerRequestType0", None],
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1alpha/projects/lpr_healthcare/locations/us/collections/default_collection/dataStores/lpr_healthcare/servingConfigs/default_search:answer",
    }

    _kwargs["json"]: Union[None, dict[str, Any]]
    if isinstance(body, AnswerRequestType0):
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
    body: Union["AnswerRequestType0", None],
) -> Response[Any]:
    """Creates Answers for searching the Longitudinal Patient Record Content

     Search with answer and follow-ups is based on the answer method. The answer method replaces the
    summarization features of the older search method and all of the features of the deprecated converse
    method. This API is a wrapper to the Google [answer](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/answer)
    API. Refer to this API for inputs/parameters.

    Args:
        body (Union['AnswerRequestType0', None]): Refer to the
            [Answer](https://cloud.google.com/generative-ai-app-
            builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer) api
            reference for supported attributes Example: {'query': 'Some example query', 'session':
            'sessionId', 'relatedQuestionsSpec': {'enable': True}, 'answerGenerationSpec':
            {'ignoreAdversarialQuery': True}, 'searchSpec': {'dataStoreSpecs': {'dataStore':
            'datastore full name'}}, 'asynchronousMode': True}.

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
    body: Union["AnswerRequestType0", None],
) -> Response[Any]:
    """Creates Answers for searching the Longitudinal Patient Record Content

     Search with answer and follow-ups is based on the answer method. The answer method replaces the
    summarization features of the older search method and all of the features of the deprecated converse
    method. This API is a wrapper to the Google [answer](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.servingConfigs/answer)
    API. Refer to this API for inputs/parameters.

    Args:
        body (Union['AnswerRequestType0', None]): Refer to the
            [Answer](https://cloud.google.com/generative-ai-app-
            builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer) api
            reference for supported attributes Example: {'query': 'Some example query', 'session':
            'sessionId', 'relatedQuestionsSpec': {'enable': True}, 'answerGenerationSpec':
            {'ignoreAdversarialQuery': True}, 'searchSpec': {'dataStoreSpecs': {'dataStore':
            'datastore full name'}}, 'asynchronousMode': True}.

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
