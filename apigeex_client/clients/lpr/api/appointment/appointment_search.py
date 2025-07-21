from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    actor: Union[Unset, str] = UNSET,
    appointment_type: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    part_status: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_category: Union[Unset, str] = UNSET,
    service_type: Union[Unset, str] = UNSET,
    slot: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    supporting_info: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["actor"] = actor

    params["appointment-type"] = appointment_type

    params["based-on"] = based_on

    params["date"] = date

    params["identifier"] = identifier

    params["location"] = location

    params["part-status"] = part_status

    params["patient"] = patient

    params["practitioner"] = practitioner

    params["reason-code"] = reason_code

    params["reason-reference"] = reason_reference

    params["service-category"] = service_category

    params["service-type"] = service_type

    params["slot"] = slot

    params["specialty"] = specialty

    params["status"] = status

    params["supporting-info"] = supporting_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Appointment",
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
    actor: Union[Unset, str] = UNSET,
    appointment_type: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    part_status: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_category: Union[Unset, str] = UNSET,
    service_type: Union[Unset, str] = UNSET,
    slot: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    supporting_info: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        actor (Union[Unset, str]):
        appointment_type (Union[Unset, str]):
        based_on (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        location (Union[Unset, str]):
        part_status (Union[Unset, str]):
        patient (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        reason_code (Union[Unset, str]):
        reason_reference (Union[Unset, str]):
        service_category (Union[Unset, str]):
        service_type (Union[Unset, str]):
        slot (Union[Unset, str]):
        specialty (Union[Unset, str]):
        status (Union[Unset, str]):
        supporting_info (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        actor=actor,
        appointment_type=appointment_type,
        based_on=based_on,
        date=date,
        identifier=identifier,
        location=location,
        part_status=part_status,
        patient=patient,
        practitioner=practitioner,
        reason_code=reason_code,
        reason_reference=reason_reference,
        service_category=service_category,
        service_type=service_type,
        slot=slot,
        specialty=specialty,
        status=status,
        supporting_info=supporting_info,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    actor: Union[Unset, str] = UNSET,
    appointment_type: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    part_status: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    practitioner: Union[Unset, str] = UNSET,
    reason_code: Union[Unset, str] = UNSET,
    reason_reference: Union[Unset, str] = UNSET,
    service_category: Union[Unset, str] = UNSET,
    service_type: Union[Unset, str] = UNSET,
    slot: Union[Unset, str] = UNSET,
    specialty: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    supporting_info: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        actor (Union[Unset, str]):
        appointment_type (Union[Unset, str]):
        based_on (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        location (Union[Unset, str]):
        part_status (Union[Unset, str]):
        patient (Union[Unset, str]):
        practitioner (Union[Unset, str]):
        reason_code (Union[Unset, str]):
        reason_reference (Union[Unset, str]):
        service_category (Union[Unset, str]):
        service_type (Union[Unset, str]):
        slot (Union[Unset, str]):
        specialty (Union[Unset, str]):
        status (Union[Unset, str]):
        supporting_info (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        actor=actor,
        appointment_type=appointment_type,
        based_on=based_on,
        date=date,
        identifier=identifier,
        location=location,
        part_status=part_status,
        patient=patient,
        practitioner=practitioner,
        reason_code=reason_code,
        reason_reference=reason_reference,
        service_category=service_category,
        service_type=service_type,
        slot=slot,
        specialty=specialty,
        status=status,
        supporting_info=supporting_info,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
