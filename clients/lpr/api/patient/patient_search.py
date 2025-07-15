from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    active: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    birthdate: Union[Unset, str] = UNSET,
    death_date: Union[Unset, str] = UNSET,
    deceased: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    family: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    general_practitioner: Union[Unset, str] = UNSET,
    given: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    link: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["active"] = active

    params["address"] = address

    params["address-city"] = address_city

    params["address-country"] = address_country

    params["address-postalcode"] = address_postalcode

    params["address-state"] = address_state

    params["address-use"] = address_use

    params["birthdate"] = birthdate

    params["death-date"] = death_date

    params["deceased"] = deceased

    params["email"] = email

    params["family"] = family

    params["gender"] = gender

    params["general-practitioner"] = general_practitioner

    params["given"] = given

    params["identifier"] = identifier

    params["language"] = language

    params["link"] = link

    params["name"] = name

    params["organization"] = organization

    params["phone"] = phone

    params["telecom"] = telecom

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Patient",
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
    active: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    birthdate: Union[Unset, str] = UNSET,
    death_date: Union[Unset, str] = UNSET,
    deceased: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    family: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    general_practitioner: Union[Unset, str] = UNSET,
    given: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    link: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        active (Union[Unset, str]):
        address (Union[Unset, str]):
        address_city (Union[Unset, str]):
        address_country (Union[Unset, str]):
        address_postalcode (Union[Unset, str]):
        address_state (Union[Unset, str]):
        address_use (Union[Unset, str]):
        birthdate (Union[Unset, str]):
        death_date (Union[Unset, str]):
        deceased (Union[Unset, str]):
        email (Union[Unset, str]):
        family (Union[Unset, str]):
        gender (Union[Unset, str]):
        general_practitioner (Union[Unset, str]):
        given (Union[Unset, str]):
        identifier (Union[Unset, str]):
        language (Union[Unset, str]):
        link (Union[Unset, str]):
        name (Union[Unset, str]):
        organization (Union[Unset, str]):
        phone (Union[Unset, str]):
        telecom (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        address=address,
        address_city=address_city,
        address_country=address_country,
        address_postalcode=address_postalcode,
        address_state=address_state,
        address_use=address_use,
        birthdate=birthdate,
        death_date=death_date,
        deceased=deceased,
        email=email,
        family=family,
        gender=gender,
        general_practitioner=general_practitioner,
        given=given,
        identifier=identifier,
        language=language,
        link=link,
        name=name,
        organization=organization,
        phone=phone,
        telecom=telecom,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    active: Union[Unset, str] = UNSET,
    address: Union[Unset, str] = UNSET,
    address_city: Union[Unset, str] = UNSET,
    address_country: Union[Unset, str] = UNSET,
    address_postalcode: Union[Unset, str] = UNSET,
    address_state: Union[Unset, str] = UNSET,
    address_use: Union[Unset, str] = UNSET,
    birthdate: Union[Unset, str] = UNSET,
    death_date: Union[Unset, str] = UNSET,
    deceased: Union[Unset, str] = UNSET,
    email: Union[Unset, str] = UNSET,
    family: Union[Unset, str] = UNSET,
    gender: Union[Unset, str] = UNSET,
    general_practitioner: Union[Unset, str] = UNSET,
    given: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    link: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    organization: Union[Unset, str] = UNSET,
    phone: Union[Unset, str] = UNSET,
    telecom: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        active (Union[Unset, str]):
        address (Union[Unset, str]):
        address_city (Union[Unset, str]):
        address_country (Union[Unset, str]):
        address_postalcode (Union[Unset, str]):
        address_state (Union[Unset, str]):
        address_use (Union[Unset, str]):
        birthdate (Union[Unset, str]):
        death_date (Union[Unset, str]):
        deceased (Union[Unset, str]):
        email (Union[Unset, str]):
        family (Union[Unset, str]):
        gender (Union[Unset, str]):
        general_practitioner (Union[Unset, str]):
        given (Union[Unset, str]):
        identifier (Union[Unset, str]):
        language (Union[Unset, str]):
        link (Union[Unset, str]):
        name (Union[Unset, str]):
        organization (Union[Unset, str]):
        phone (Union[Unset, str]):
        telecom (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        active=active,
        address=address,
        address_city=address_city,
        address_country=address_country,
        address_postalcode=address_postalcode,
        address_state=address_state,
        address_use=address_use,
        birthdate=birthdate,
        death_date=death_date,
        deceased=deceased,
        email=email,
        family=family,
        gender=gender,
        general_practitioner=general_practitioner,
        given=given,
        identifier=identifier,
        language=language,
        link=link,
        name=name,
        organization=organization,
        phone=phone,
        telecom=telecom,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
