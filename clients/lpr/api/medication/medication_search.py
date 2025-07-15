from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: Union[Unset, str] = UNSET,
    expiration_date: Union[Unset, str] = UNSET,
    form: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    ingredient: Union[Unset, str] = UNSET,
    ingredient_code: Union[Unset, str] = UNSET,
    lot_number: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["expiration-date"] = expiration_date

    params["form"] = form

    params["identifier"] = identifier

    params["ingredient"] = ingredient

    params["ingredient-code"] = ingredient_code

    params["lot-number"] = lot_number

    params["manufacturer"] = manufacturer

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Medication",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
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
    code: Union[Unset, str] = UNSET,
    expiration_date: Union[Unset, str] = UNSET,
    form: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    ingredient: Union[Unset, str] = UNSET,
    ingredient_code: Union[Unset, str] = UNSET,
    lot_number: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        expiration_date (Union[Unset, str]):
        form (Union[Unset, str]):
        identifier (Union[Unset, str]):
        ingredient (Union[Unset, str]):
        ingredient_code (Union[Unset, str]):
        lot_number (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        expiration_date=expiration_date,
        form=form,
        identifier=identifier,
        ingredient=ingredient,
        ingredient_code=ingredient_code,
        lot_number=lot_number,
        manufacturer=manufacturer,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    expiration_date: Union[Unset, str] = UNSET,
    form: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    ingredient: Union[Unset, str] = UNSET,
    ingredient_code: Union[Unset, str] = UNSET,
    lot_number: Union[Unset, str] = UNSET,
    manufacturer: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        expiration_date (Union[Unset, str]):
        form (Union[Unset, str]):
        identifier (Union[Unset, str]):
        ingredient (Union[Unset, str]):
        ingredient_code (Union[Unset, str]):
        lot_number (Union[Unset, str]):
        manufacturer (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        expiration_date=expiration_date,
        form=form,
        identifier=identifier,
        ingredient=ingredient,
        ingredient_code=ingredient_code,
        lot_number=lot_number,
        manufacturer=manufacturer,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
