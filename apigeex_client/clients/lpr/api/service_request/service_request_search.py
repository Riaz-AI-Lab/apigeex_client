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
    encounter: Union[Unset, str] = UNSET,
    authored: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    instantiates_canonical: Union[Unset, str] = UNSET,
    instantiates_uri: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    occurrence: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    performer_type: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    replaces: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    requisition: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["identifier"] = identifier

    params["patient"] = patient

    params["encounter"] = encounter

    params["authored"] = authored

    params["based-on"] = based_on

    params["body-site"] = body_site

    params["category"] = category

    params["instantiates-canonical"] = instantiates_canonical

    params["instantiates-uri"] = instantiates_uri

    params["intent"] = intent

    params["occurrence"] = occurrence

    params["performer"] = performer

    params["performer-type"] = performer_type

    params["priority"] = priority

    params["replaces"] = replaces

    params["requester"] = requester

    params["requisition"] = requisition

    params["specimen"] = specimen

    params["status"] = status

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ServiceRequest",
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
    encounter: Union[Unset, str] = UNSET,
    authored: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    instantiates_canonical: Union[Unset, str] = UNSET,
    instantiates_uri: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    occurrence: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    performer_type: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    replaces: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    requisition: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        encounter (Union[Unset, str]):
        authored (Union[Unset, str]):
        based_on (Union[Unset, str]):
        body_site (Union[Unset, str]):
        category (Union[Unset, str]):
        instantiates_canonical (Union[Unset, str]):
        instantiates_uri (Union[Unset, str]):
        intent (Union[Unset, str]):
        occurrence (Union[Unset, str]):
        performer (Union[Unset, str]):
        performer_type (Union[Unset, str]):
        priority (Union[Unset, str]):
        replaces (Union[Unset, str]):
        requester (Union[Unset, str]):
        requisition (Union[Unset, str]):
        specimen (Union[Unset, str]):
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
        encounter=encounter,
        authored=authored,
        based_on=based_on,
        body_site=body_site,
        category=category,
        instantiates_canonical=instantiates_canonical,
        instantiates_uri=instantiates_uri,
        intent=intent,
        occurrence=occurrence,
        performer=performer,
        performer_type=performer_type,
        priority=priority,
        replaces=replaces,
        requester=requester,
        requisition=requisition,
        specimen=specimen,
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
    encounter: Union[Unset, str] = UNSET,
    authored: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    body_site: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    instantiates_canonical: Union[Unset, str] = UNSET,
    instantiates_uri: Union[Unset, str] = UNSET,
    intent: Union[Unset, str] = UNSET,
    occurrence: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    performer_type: Union[Unset, str] = UNSET,
    priority: Union[Unset, str] = UNSET,
    replaces: Union[Unset, str] = UNSET,
    requester: Union[Unset, str] = UNSET,
    requisition: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        encounter (Union[Unset, str]):
        authored (Union[Unset, str]):
        based_on (Union[Unset, str]):
        body_site (Union[Unset, str]):
        category (Union[Unset, str]):
        instantiates_canonical (Union[Unset, str]):
        instantiates_uri (Union[Unset, str]):
        intent (Union[Unset, str]):
        occurrence (Union[Unset, str]):
        performer (Union[Unset, str]):
        performer_type (Union[Unset, str]):
        priority (Union[Unset, str]):
        replaces (Union[Unset, str]):
        requester (Union[Unset, str]):
        requisition (Union[Unset, str]):
        specimen (Union[Unset, str]):
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
        encounter=encounter,
        authored=authored,
        based_on=based_on,
        body_site=body_site,
        category=category,
        instantiates_canonical=instantiates_canonical,
        instantiates_uri=instantiates_uri,
        intent=intent,
        occurrence=occurrence,
        performer=performer,
        performer_type=performer_type,
        priority=priority,
        replaces=replaces,
        requester=requester,
        requisition=requisition,
        specimen=specimen,
        status=status,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
