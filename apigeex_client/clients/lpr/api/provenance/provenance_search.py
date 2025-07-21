from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    agent: Union[Unset, str] = UNSET,
    agent_role: Union[Unset, str] = UNSET,
    agent_type: Union[Unset, str] = UNSET,
    entity: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorded: Union[Unset, str] = UNSET,
    signature_type: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    when: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["agent"] = agent

    params["agent-role"] = agent_role

    params["agent-type"] = agent_type

    params["entity"] = entity

    params["location"] = location

    params["patient"] = patient

    params["recorded"] = recorded

    params["signature-type"] = signature_type

    params["target"] = target

    params["when"] = when

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Provenance",
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
    agent: Union[Unset, str] = UNSET,
    agent_role: Union[Unset, str] = UNSET,
    agent_type: Union[Unset, str] = UNSET,
    entity: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorded: Union[Unset, str] = UNSET,
    signature_type: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    when: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        agent (Union[Unset, str]):
        agent_role (Union[Unset, str]):
        agent_type (Union[Unset, str]):
        entity (Union[Unset, str]):
        location (Union[Unset, str]):
        patient (Union[Unset, str]):
        recorded (Union[Unset, str]):
        signature_type (Union[Unset, str]):
        target (Union[Unset, str]):
        when (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agent=agent,
        agent_role=agent_role,
        agent_type=agent_type,
        entity=entity,
        location=location,
        patient=patient,
        recorded=recorded,
        signature_type=signature_type,
        target=target,
        when=when,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    agent: Union[Unset, str] = UNSET,
    agent_role: Union[Unset, str] = UNSET,
    agent_type: Union[Unset, str] = UNSET,
    entity: Union[Unset, str] = UNSET,
    location: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    recorded: Union[Unset, str] = UNSET,
    signature_type: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    when: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        agent (Union[Unset, str]):
        agent_role (Union[Unset, str]):
        agent_type (Union[Unset, str]):
        entity (Union[Unset, str]):
        location (Union[Unset, str]):
        patient (Union[Unset, str]):
        recorded (Union[Unset, str]):
        signature_type (Union[Unset, str]):
        target (Union[Unset, str]):
        when (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        agent=agent,
        agent_role=agent_role,
        agent_type=agent_type,
        entity=entity,
        location=location,
        patient=patient,
        recorded=recorded,
        signature_type=signature_type,
        target=target,
        when=when,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
