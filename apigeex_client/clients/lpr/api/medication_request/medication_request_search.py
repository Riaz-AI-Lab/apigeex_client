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
    medication: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    authoredon: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    intended_dispenser: Union[Unset, str] = UNSET,
    intended_performer: Union[Unset, str] = UNSET,
    intended_performertype: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["identifier"] = identifier

    params["patient"] = patient

    params["medication"] = medication

    params["status"] = status

    params["authoredon"] = authoredon

    params["category"] = category

    params["date"] = date

    params["encounter"] = encounter

    params["intended-dispenser"] = intended_dispenser

    params["intended-performer"] = intended_performer

    params["intended-performertype"] = intended_performertype

    params["intent"] = intent

    params["priority"] = priority

    params["requester"] = requester

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/MedicationRequest",
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
    medication: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    authoredon: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    intended_dispenser: Union[Unset, str] = UNSET,
    intended_performer: Union[Unset, str] = UNSET,
    intended_performertype: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        medication (Union[Unset, str]):
        status (Union[Unset, str]):
        authoredon (Union[Unset, str]):
        category (Union[Unset, str]):
        date (Union[Unset, str]):
        encounter (Union[Unset, str]):
        intended_dispenser (Union[Unset, str]):
        intended_performer (Union[Unset, str]):
        intended_performertype (Union[Unset, str]):
        intent (Union[Unset, str]):
        priority (Union[Unset, str]):
        requester (Union[Unset, str]):
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
        medication=medication,
        status=status,
        authoredon=authoredon,
        category=category,
        date=date,
        encounter=encounter,
        intended_dispenser=intended_dispenser,
        intended_performer=intended_performer,
        intended_performertype=intended_performertype,
        intent=intent,
        priority=priority,
        requester=requester,
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
    medication: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    authoredon: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    intended_dispenser: Union[Unset, str] = UNSET,
    intended_performer: Union[Unset, str] = UNSET,
    intended_performertype: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        medication (Union[Unset, str]):
        status (Union[Unset, str]):
        authoredon (Union[Unset, str]):
        category (Union[Unset, str]):
        date (Union[Unset, str]):
        encounter (Union[Unset, str]):
        intended_dispenser (Union[Unset, str]):
        intended_performer (Union[Unset, str]):
        intended_performertype (Union[Unset, str]):
        intent (Union[Unset, str]):
        priority (Union[Unset, str]):
        requester (Union[Unset, str]):
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
        medication=medication,
        status=status,
        authoredon=authoredon,
        category=category,
        date=date,
        encounter=encounter,
        intended_dispenser=intended_dispenser,
        intended_performer=intended_performer,
        intended_performertype=intended_performertype,
        intent=intent,
        priority=priority,
        requester=requester,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
