from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.study_response import StudyResponse
from ...types import Response


def _get_kwargs(
    nct_number: Any,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/v1/nctNumber/{nct_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, StudyResponse]]:
    if response.status_code == 200:
        response_200 = StudyResponse.from_dict(response.json())

        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, StudyResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    nct_number: Any,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, StudyResponse]]:
    """Studybynctnumber

     Search for a study by the NCT number.

    Args:
        nct_number (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, StudyResponse]]
    """

    kwargs = _get_kwargs(
        nct_number=nct_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    nct_number: Any,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, StudyResponse]]:
    """Studybynctnumber

     Search for a study by the NCT number.

    Args:
        nct_number (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, StudyResponse]
    """

    return sync_detailed(
        nct_number=nct_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    nct_number: Any,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[HTTPValidationError, StudyResponse]]:
    """Studybynctnumber

     Search for a study by the NCT number.

    Args:
        nct_number (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, StudyResponse]]
    """

    kwargs = _get_kwargs(
        nct_number=nct_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    nct_number: Any,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[HTTPValidationError, StudyResponse]]:
    """Studybynctnumber

     Search for a study by the NCT number.

    Args:
        nct_number (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, StudyResponse]
    """

    return (
        await asyncio_detailed(
            nct_number=nct_number,
            client=client,
        )
    ).parsed
