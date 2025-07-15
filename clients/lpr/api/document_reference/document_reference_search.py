from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    authenticator: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    contenttype: Union[Unset, str] = UNSET,
    custodian: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    facility: Union[Unset, str] = UNSET,
    format_: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
    related: Union[Unset, str] = UNSET,
    relatesto: Union[Unset, str] = UNSET,
    relation: Union[Unset, str] = UNSET,
    security_label: Union[Unset, str] = UNSET,
    setting: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    relationship: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["identifier"] = identifier

    params["patient"] = patient

    params["type"] = type_

    params["encounter"] = encounter

    params["authenticator"] = authenticator

    params["author"] = author

    params["category"] = category

    params["contenttype"] = contenttype

    params["custodian"] = custodian

    params["date"] = date

    params["description"] = description

    params["event"] = event

    params["facility"] = facility

    params["format"] = format_

    params["language"] = language

    params["location"] = location

    params["period"] = period

    params["related"] = related

    params["relatesto"] = relatesto

    params["relation"] = relation

    params["security-label"] = security_label

    params["setting"] = setting

    params["status"] = status

    params["subject"] = subject

    params["relationship"] = relationship

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/DocumentReference",
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
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    authenticator: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    contenttype: Union[Unset, str] = UNSET,
    custodian: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    facility: Union[Unset, str] = UNSET,
    format_: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
    related: Union[Unset, str] = UNSET,
    relatesto: Union[Unset, str] = UNSET,
    relation: Union[Unset, str] = UNSET,
    security_label: Union[Unset, str] = UNSET,
    setting: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    relationship: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        type_ (Union[Unset, str]):
        encounter (Union[Unset, str]):
        authenticator (Union[Unset, str]):
        author (Union[Unset, str]):
        category (Union[Unset, str]):
        contenttype (Union[Unset, str]):
        custodian (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        event (Union[Unset, str]):
        facility (Union[Unset, str]):
        format_ (Union[Unset, str]):
        language (Union[Unset, str]):
        location (Union[Unset, str]):
        period (Union[Unset, str]):
        related (Union[Unset, str]):
        relatesto (Union[Unset, str]):
        relation (Union[Unset, str]):
        security_label (Union[Unset, str]):
        setting (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):
        relationship (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        patient=patient,
        type_=type_,
        encounter=encounter,
        authenticator=authenticator,
        author=author,
        category=category,
        contenttype=contenttype,
        custodian=custodian,
        date=date,
        description=description,
        event=event,
        facility=facility,
        format_=format_,
        language=language,
        location=location,
        period=period,
        related=related,
        relatesto=relatesto,
        relation=relation,
        security_label=security_label,
        setting=setting,
        status=status,
        subject=subject,
        relationship=relationship,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    authenticator: Union[Unset, str] = UNSET,
    author: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    contenttype: Union[Unset, str] = UNSET,
    custodian: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    event: Union[Unset, str] = UNSET,
    facility: Union[Unset, str] = UNSET,
    format_: Union[Unset, str] = UNSET,
    language: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    period: Union[Unset, str] = UNSET,
    related: Union[Unset, str] = UNSET,
    relatesto: Union[Unset, str] = UNSET,
    relation: Union[Unset, str] = UNSET,
    security_label: Union[Unset, str] = UNSET,
    setting: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    relationship: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        type_ (Union[Unset, str]):
        encounter (Union[Unset, str]):
        authenticator (Union[Unset, str]):
        author (Union[Unset, str]):
        category (Union[Unset, str]):
        contenttype (Union[Unset, str]):
        custodian (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        event (Union[Unset, str]):
        facility (Union[Unset, str]):
        format_ (Union[Unset, str]):
        language (Union[Unset, str]):
        location (Union[Unset, str]):
        period (Union[Unset, str]):
        related (Union[Unset, str]):
        relatesto (Union[Unset, str]):
        relation (Union[Unset, str]):
        security_label (Union[Unset, str]):
        setting (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):
        relationship (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        patient=patient,
        type_=type_,
        encounter=encounter,
        authenticator=authenticator,
        author=author,
        category=category,
        contenttype=contenttype,
        custodian=custodian,
        date=date,
        description=description,
        event=event,
        facility=facility,
        format_=format_,
        language=language,
        location=location,
        period=period,
        related=related,
        relatesto=relatesto,
        relation=relation,
        security_label=security_label,
        setting=setting,
        status=status,
        subject=subject,
        relationship=relationship,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
