from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    operational_status: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    partof: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["address"] = address

    params["address-city"] = address_city

    params["address-country"] = address_country

    params["address-postalcode"] = address_postalcode

    params["address-state"] = address_state

    params["address-use"] = address_use

    params["endpoint"] = endpoint

    params["identifier"] = identifier

    params["name"] = name

    params["operational-status"] = operational_status

    params["organization"] = organization

    params["partof"] = partof

    params["status"] = status

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Location",
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
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    operational_status: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    partof: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        address (Union[Unset, str]):
        address_city (Union[Unset, str]):
        address_country (Union[Unset, str]):
        address_postalcode (Union[Unset, str]):
        address_state (Union[Unset, str]):
        address_use (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        operational_status (Union[Unset, str]):
        organization (Union[Unset, str]):
        partof (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        address=address,
        address_city=address_city,
        address_country=address_country,
        address_postalcode=address_postalcode,
        address_state=address_state,
        address_use=address_use,
        endpoint=endpoint,
        identifier=identifier,
        name=name,
        operational_status=operational_status,
        organization=organization,
        partof=partof,
        status=status,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    operational_status: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    partof: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        address (Union[Unset, str]):
        address_city (Union[Unset, str]):
        address_country (Union[Unset, str]):
        address_postalcode (Union[Unset, str]):
        address_state (Union[Unset, str]):
        address_use (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        identifier (Union[Unset, str]):
        name (Union[Unset, str]):
        operational_status (Union[Unset, str]):
        organization (Union[Unset, str]):
        partof (Union[Unset, str]):
        status (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        address=address,
        address_city=address_city,
        address_country=address_country,
        address_postalcode=address_postalcode,
        address_state=address_state,
        address_use=address_use,
        endpoint=endpoint,
        identifier=identifier,
        name=name,
        operational_status=operational_status,
        organization=organization,
        partof=partof,
        status=status,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
