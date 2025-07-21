from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    effective_time: Union[Unset, str] = UNSET,
    medication: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason_given: Union[Unset, str] = UNSET,
    reason_not_given: Union[Unset, str] = UNSET,
    request: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["identifier"] = identifier

    params["patient"] = patient

    params["context"] = context

    params["device"] = device

    params["effective-time"] = effective_time

    params["medication"] = medication

    params["performer"] = performer

    params["reason-given"] = reason_given

    params["reason-not-given"] = reason_not_given

    params["request"] = request

    params["status"] = status

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/MedicationAdministration",
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
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    effective_time: Union[Unset, str] = UNSET,
    medication: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason_given: Union[Unset, str] = UNSET,
    reason_not_given: Union[Unset, str] = UNSET,
    request: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        context (Union[Unset, str]):
        device (Union[Unset, str]):
        effective_time (Union[Unset, str]):
        medication (Union[Unset, str]):
        performer (Union[Unset, str]):
        reason_given (Union[Unset, str]):
        reason_not_given (Union[Unset, str]):
        request (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        identifier=identifier,
        patient=patient,
        context=context,
        device=device,
        effective_time=effective_time,
        medication=medication,
        performer=performer,
        reason_given=reason_given,
        reason_not_given=reason_not_given,
        request=request,
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
    code: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    context: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    effective_time: Union[Unset, str] = UNSET,
    medication: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason_given: Union[Unset, str] = UNSET,
    reason_not_given: Union[Unset, str] = UNSET,
    request: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        context (Union[Unset, str]):
        device (Union[Unset, str]):
        effective_time (Union[Unset, str]):
        medication (Union[Unset, str]):
        performer (Union[Unset, str]):
        reason_given (Union[Unset, str]):
        reason_not_given (Union[Unset, str]):
        request (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        identifier=identifier,
        patient=patient,
        context=context,
        device=device,
        effective_time=effective_time,
        medication=medication,
        performer=performer,
        reason_given=reason_given,
        reason_not_given=reason_not_given,
        request=request,
        status=status,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
