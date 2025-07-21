from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    appointment: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    diagnosis: Union[Unset, str] = UNSET,
    episode_of_care: Union[Unset, str] = UNSET,
    length: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    location_period: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    participant: Union[Unset, str] = UNSET,
    participant_type: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_provider: Union[Unset, str] = UNSET,
    special_arrangement: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["date"] = date

    params["identifier"] = identifier

    params["patient"] = patient

    params["type"] = type_

    params["account"] = account

    params["appointment"] = appointment

    params["based-on"] = based_on

    params["class"] = class_

    params["diagnosis"] = diagnosis

    params["episode-of-care"] = episode_of_care

    params["length"] = length

    params["location"] = location

    params["location-period"] = location_period

    params["part-of"] = part_of

    params["participant"] = participant

    params["participant-type"] = participant_type

    params["practitioner"] = practitioner

    params["reason-code"] = reason_code

    params["reason-reference"] = reason_reference

    params["service-provider"] = service_provider

    params["special-arrangement"] = special_arrangement

    params["status"] = status

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Encounter",
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
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    appointment: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    diagnosis: Union[Unset, str] = UNSET,
    episode_of_care: Union[Unset, str] = UNSET,
    length: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    location_period: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    participant: Union[Unset, str] = UNSET,
    participant_type: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_provider: Union[Unset, str] = UNSET,
    special_arrangement: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        type_ (Union[Unset, str]):
        account (Union[Unset, str]):
        appointment (Union[Unset, str]):
        based_on (Union[Unset, str]):
        class_ (Union[Unset, str]):
        diagnosis (Union[Unset, str]):
        episode_of_care (Union[Unset, str]):
        length (Union[Unset, str]):
        location (Union[Unset, str]):
        location_period (Union[Unset, str]):
        part_of (Union[Unset, str]):
        participant (Union[Unset, str]):
        participant_type (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        reason_code (Union[Unset, str]):
        reason_reference (Union[Unset, str]):
        service_provider (Union[Unset, str]):
        special_arrangement (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        date=date,
        identifier=identifier,
        patient=patient,
        type_=type_,
        account=account,
        appointment=appointment,
        based_on=based_on,
        class_=class_,
        diagnosis=diagnosis,
        episode_of_care=episode_of_care,
        length=length,
        location=location,
        location_period=location_period,
        part_of=part_of,
        participant=participant,
        participant_type=participant_type,
        practitioner=practitioner,
        reason_code=reason_code,
        reason_reference=reason_reference,
        service_provider=service_provider,
        special_arrangement=special_arrangement,
        status=status,
        subject=subject,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    account: Union[Unset, str] = UNSET,
    appointment: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    class_: Union[Unset, str] = UNSET,
    diagnosis: Union[Unset, str] = UNSET,
    episode_of_care: Union[Unset, str] = UNSET,
    length: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    location_period: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    participant: Union[Unset, str] = UNSET,
    participant_type: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_provider: Union[Unset, str] = UNSET,
    special_arrangement: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        type_ (Union[Unset, str]):
        account (Union[Unset, str]):
        appointment (Union[Unset, str]):
        based_on (Union[Unset, str]):
        class_ (Union[Unset, str]):
        diagnosis (Union[Unset, str]):
        episode_of_care (Union[Unset, str]):
        length (Union[Unset, str]):
        location (Union[Unset, str]):
        location_period (Union[Unset, str]):
        part_of (Union[Unset, str]):
        participant (Union[Unset, str]):
        participant_type (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        reason_code (Union[Unset, str]):
        reason_reference (Union[Unset, str]):
        service_provider (Union[Unset, str]):
        special_arrangement (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        date=date,
        identifier=identifier,
        patient=patient,
        type_=type_,
        account=account,
        appointment=appointment,
        based_on=based_on,
        class_=class_,
        diagnosis=diagnosis,
        episode_of_care=episode_of_care,
        length=length,
        location=location,
        location_period=location_period,
        part_of=part_of,
        participant=participant,
        participant_type=participant_type,
        practitioner=practitioner,
        reason_code=reason_code,
        reason_reference=reason_reference,
        service_provider=service_provider,
        special_arrangement=special_arrangement,
        status=status,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
