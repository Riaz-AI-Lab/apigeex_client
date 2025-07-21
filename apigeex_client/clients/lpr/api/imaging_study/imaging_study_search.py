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
    basedon: Union[Unset, str] = UNSET,
    bodysite: Union[Unset, str] = UNSET,
    dicom_class: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    interpreter: Union[Unset, str] = UNSET,
    modality: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason: Union[Unset, str] = UNSET,
    referrer: Union[Unset, str] = UNSET,
    series: Union[Unset, str] = UNSET,
    started: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["identifier"] = identifier

    params["patient"] = patient

    params["basedon"] = basedon

    params["bodysite"] = bodysite

    params["dicom-class"] = dicom_class

    params["encounter"] = encounter

    params["endpoint"] = endpoint

    params["instance"] = instance

    params["interpreter"] = interpreter

    params["modality"] = modality

    params["performer"] = performer

    params["reason"] = reason

    params["referrer"] = referrer

    params["series"] = series

    params["started"] = started

    params["status"] = status

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ImagingStudy",
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
    basedon: Union[Unset, str] = UNSET,
    bodysite: Union[Unset, str] = UNSET,
    dicom_class: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    interpreter: Union[Unset, str] = UNSET,
    modality: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason: Union[Unset, str] = UNSET,
    referrer: Union[Unset, str] = UNSET,
    series: Union[Unset, str] = UNSET,
    started: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        basedon (Union[Unset, str]):
        bodysite (Union[Unset, str]):
        dicom_class (Union[Unset, str]):
        encounter (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        instance (Union[Unset, str]):
        interpreter (Union[Unset, str]):
        modality (Union[Unset, str]):
        performer (Union[Unset, str]):
        reason (Union[Unset, str]):
        referrer (Union[Unset, str]):
        series (Union[Unset, str]):
        started (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        patient=patient,
        basedon=basedon,
        bodysite=bodysite,
        dicom_class=dicom_class,
        encounter=encounter,
        endpoint=endpoint,
        instance=instance,
        interpreter=interpreter,
        modality=modality,
        performer=performer,
        reason=reason,
        referrer=referrer,
        series=series,
        started=started,
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
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    basedon: Union[Unset, str] = UNSET,
    bodysite: Union[Unset, str] = UNSET,
    dicom_class: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    endpoint: Union[Unset, str] = UNSET,
    instance: Union[Unset, str] = UNSET,
    interpreter: Union[Unset, str] = UNSET,
    modality: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    reason: Union[Unset, str] = UNSET,
    referrer: Union[Unset, str] = UNSET,
    series: Union[Unset, str] = UNSET,
    started: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        basedon (Union[Unset, str]):
        bodysite (Union[Unset, str]):
        dicom_class (Union[Unset, str]):
        encounter (Union[Unset, str]):
        endpoint (Union[Unset, str]):
        instance (Union[Unset, str]):
        interpreter (Union[Unset, str]):
        modality (Union[Unset, str]):
        performer (Union[Unset, str]):
        reason (Union[Unset, str]):
        referrer (Union[Unset, str]):
        series (Union[Unset, str]):
        started (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        patient=patient,
        basedon=basedon,
        bodysite=bodysite,
        dicom_class=dicom_class,
        encounter=encounter,
        endpoint=endpoint,
        instance=instance,
        interpreter=interpreter,
        modality=modality,
        performer=performer,
        reason=reason,
        referrer=referrer,
        series=series,
        started=started,
        status=status,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
