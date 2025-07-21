from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    email: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
    active: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["email"] = email

    params["phone"] = phone

    params["telecom"] = telecom

    params["active"] = active

    params["date"] = date

    params["endpoint"] = endpoint

    params["identifier"] = identifier

    params["location"] = location

    params["organization"] = organization

    params["practitioner"] = practitioner

    params["role"] = role

    params["service"] = service

    params["specialty"] = specialty

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/PractitionerRole",
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
    email: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
    active: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        telecom (Union[Unset, str]):
        active (Union[Unset, str]):
        date (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        identifier (Union[Unset, str]):
        location (Union[Unset, str]):
        organization (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        role (Union[Unset, str]):
        service (Union[Unset, str]):
        specialty (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        phone=phone,
        telecom=telecom,
        active=active,
        date=date,
        endpoint=endpoint,
        identifier=identifier,
        location=location,
        organization=organization,
        practitioner=practitioner,
        role=role,
        service=service,
        specialty=specialty,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    email: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
    active: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        email (Union[Unset, str]):
        phone (Union[Unset, str]):
        telecom (Union[Unset, str]):
        active (Union[Unset, str]):
        date (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        identifier (Union[Unset, str]):
        location (Union[Unset, str]):
        organization (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        role (Union[Unset, str]):
        service (Union[Unset, str]):
        specialty (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        email=email,
        phone=phone,
        telecom=telecom,
        active=active,
        date=date,
        endpoint=endpoint,
        identifier=identifier,
        location=location,
        organization=organization,
        practitioner=practitioner,
        role=role,
        service=service,
        specialty=specialty,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
