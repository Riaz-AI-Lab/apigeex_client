from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    asserter: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    criticality: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    last_date: Union[Unset, str] = UNSET,
    manifestation: Union[Unset, str] = UNSET,
    onset: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorder: Union[Unset, str] = UNSET,
    route: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["asserter"] = asserter

    params["category"] = category

    params["clinical-status"] = clinical_status

    params["code"] = code

    params["criticality"] = criticality

    params["date"] = date

    params["identifier"] = identifier

    params["last-date"] = last_date

    params["manifestation"] = manifestation

    params["onset"] = onset

    params["patient"] = patient

    params["recorder"] = recorder

    params["route"] = route

    params["severity"] = severity

    params["type"] = type_

    params["verification-status"] = verification_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/AllergyIntolerance",
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
    asserter: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    criticality: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    last_date: Union[Unset, str] = UNSET,
    manifestation: Union[Unset, str] = UNSET,
    onset: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorder: Union[Unset, str] = UNSET,
    route: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        asserter (Union[Unset, str]):
        category (Union[Unset, str]):
        clinical_status (Union[Unset, str]):
        code (Union[Unset, str]):
        criticality (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        last_date (Union[Unset, str]):
        manifestation (Union[Unset, str]):
        onset (Union[Unset, str]):
        patient (Union[Unset, str]):
        recorder (Union[Unset, str]):
        route (Union[Unset, str]):
        severity (Union[Unset, str]):
        type_ (Union[Unset, str]):
        verification_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asserter=asserter,
        category=category,
        clinical_status=clinical_status,
        code=code,
        criticality=criticality,
        date=date,
        identifier=identifier,
        last_date=last_date,
        manifestation=manifestation,
        onset=onset,
        patient=patient,
        recorder=recorder,
        route=route,
        severity=severity,
        type_=type_,
        verification_status=verification_status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    asserter: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    criticality: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    last_date: Union[Unset, str] = UNSET,
    manifestation: Union[Unset, str] = UNSET,
    onset: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorder: Union[Unset, str] = UNSET,
    route: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        asserter (Union[Unset, str]):
        category (Union[Unset, str]):
        clinical_status (Union[Unset, str]):
        code (Union[Unset, str]):
        criticality (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        last_date (Union[Unset, str]):
        manifestation (Union[Unset, str]):
        onset (Union[Unset, str]):
        patient (Union[Unset, str]):
        recorder (Union[Unset, str]):
        route (Union[Unset, str]):
        severity (Union[Unset, str]):
        type_ (Union[Unset, str]):
        verification_status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        asserter=asserter,
        category=category,
        clinical_status=clinical_status,
        code=code,
        criticality=criticality,
        date=date,
        identifier=identifier,
        last_date=last_date,
        manifestation=manifestation,
        onset=onset,
        patient=patient,
        recorder=recorder,
        route=route,
        severity=severity,
        type_=type_,
        verification_status=verification_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
