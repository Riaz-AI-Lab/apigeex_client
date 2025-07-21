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
    abatement_age: Union[Unset, str] = UNSET,
    abatement_date: Union[Unset, str] = UNSET,
    abatement_string: Union[Unset, str] = UNSET,
    asserter: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    evidence: Union[Unset, str] = UNSET,
    evidence_detail: Union[Unset, str] = UNSET,
    onset_age: Union[Unset, str] = UNSET,
    onset_date: Union[Unset, str] = UNSET,
    onset_info: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    stage: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["identifier"] = identifier

    params["patient"] = patient

    params["abatement-age"] = abatement_age

    params["abatement-date"] = abatement_date

    params["abatement-string"] = abatement_string

    params["asserter"] = asserter

    params["body-site"] = body_site

    params["category"] = category

    params["clinical-status"] = clinical_status

    params["encounter"] = encounter

    params["evidence"] = evidence

    params["evidence-detail"] = evidence_detail

    params["onset-age"] = onset_age

    params["onset-date"] = onset_date

    params["onset-info"] = onset_info

    params["recorded-date"] = recorded_date

    params["severity"] = severity

    params["stage"] = stage

    params["subject"] = subject

    params["verification-status"] = verification_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Condition",
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
    abatement_age: Union[Unset, str] = UNSET,
    abatement_date: Union[Unset, str] = UNSET,
    abatement_string: Union[Unset, str] = UNSET,
    asserter: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    evidence: Union[Unset, str] = UNSET,
    evidence_detail: Union[Unset, str] = UNSET,
    onset_age: Union[Unset, str] = UNSET,
    onset_date: Union[Unset, str] = UNSET,
    onset_info: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    stage: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        abatement_age (Union[Unset, str]):
        abatement_date (Union[Unset, str]):
        abatement_string (Union[Unset, str]):
        asserter (Union[Unset, str]):
        body_site (Union[Unset, str]):
        category (Union[Unset, str]):
        clinical_status (Union[Unset, str]):
        encounter (Union[Unset, str]):
        evidence (Union[Unset, str]):
        evidence_detail (Union[Unset, str]):
        onset_age (Union[Unset, str]):
        onset_date (Union[Unset, str]):
        onset_info (Union[Unset, str]):
        recorded_date (Union[Unset, str]):
        severity (Union[Unset, str]):
        stage (Union[Unset, str]):
        subject (Union[Unset, str]):
        verification_status (Union[Unset, str]):

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
        abatement_age=abatement_age,
        abatement_date=abatement_date,
        abatement_string=abatement_string,
        asserter=asserter,
        body_site=body_site,
        category=category,
        clinical_status=clinical_status,
        encounter=encounter,
        evidence=evidence,
        evidence_detail=evidence_detail,
        onset_age=onset_age,
        onset_date=onset_date,
        onset_info=onset_info,
        recorded_date=recorded_date,
        severity=severity,
        stage=stage,
        subject=subject,
        verification_status=verification_status,
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
    abatement_age: Union[Unset, str] = UNSET,
    abatement_date: Union[Unset, str] = UNSET,
    abatement_string: Union[Unset, str] = UNSET,
    asserter: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    clinical_status: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    evidence: Union[Unset, str] = UNSET,
    evidence_detail: Union[Unset, str] = UNSET,
    onset_age: Union[Unset, str] = UNSET,
    onset_date: Union[Unset, str] = UNSET,
    onset_info: Union[Unset, str] = UNSET,
    recorded_date: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    stage: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    verification_status: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        abatement_age (Union[Unset, str]):
        abatement_date (Union[Unset, str]):
        abatement_string (Union[Unset, str]):
        asserter (Union[Unset, str]):
        body_site (Union[Unset, str]):
        category (Union[Unset, str]):
        clinical_status (Union[Unset, str]):
        encounter (Union[Unset, str]):
        evidence (Union[Unset, str]):
        evidence_detail (Union[Unset, str]):
        onset_age (Union[Unset, str]):
        onset_date (Union[Unset, str]):
        onset_info (Union[Unset, str]):
        recorded_date (Union[Unset, str]):
        severity (Union[Unset, str]):
        stage (Union[Unset, str]):
        subject (Union[Unset, str]):
        verification_status (Union[Unset, str]):

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
        abatement_age=abatement_age,
        abatement_date=abatement_date,
        abatement_string=abatement_string,
        asserter=asserter,
        body_site=body_site,
        category=category,
        clinical_status=clinical_status,
        encounter=encounter,
        evidence=evidence,
        evidence_detail=evidence_detail,
        onset_age=onset_age,
        onset_date=onset_date,
        onset_info=onset_info,
        recorded_date=recorded_date,
        severity=severity,
        stage=stage,
        subject=subject,
        verification_status=verification_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
