from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    beneficiary: Union[Unset, str] = UNSET,
    class_type: Union[Unset, str] = UNSET,
    class_value: Union[Unset, str] = UNSET,
    dependent: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    payor: Union[Unset, str] = UNSET,
    policy_holder: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["beneficiary"] = beneficiary

    params["class-type"] = class_type

    params["class-value"] = class_value

    params["dependent"] = dependent

    params["identifier"] = identifier

    params["patient"] = patient

    params["payor"] = payor

    params["policy-holder"] = policy_holder

    params["status"] = status

    params["subscriber"] = subscriber

    params["type"] = type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Coverage",
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
    beneficiary: Union[Unset, str] = UNSET,
    class_type: Union[Unset, str] = UNSET,
    class_value: Union[Unset, str] = UNSET,
    dependent: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    payor: Union[Unset, str] = UNSET,
    policy_holder: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        beneficiary (Union[Unset, str]):
        class_type (Union[Unset, str]):
        class_value (Union[Unset, str]):
        dependent (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        payor (Union[Unset, str]):
        policy_holder (Union[Unset, str]):
        status (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        beneficiary=beneficiary,
        class_type=class_type,
        class_value=class_value,
        dependent=dependent,
        identifier=identifier,
        patient=patient,
        payor=payor,
        policy_holder=policy_holder,
        status=status,
        subscriber=subscriber,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    beneficiary: Union[Unset, str] = UNSET,
    class_type: Union[Unset, str] = UNSET,
    class_value: Union[Unset, str] = UNSET,
    dependent: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    payor: Union[Unset, str] = UNSET,
    policy_holder: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subscriber: Union[Unset, str] = UNSET,
    type_: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        beneficiary (Union[Unset, str]):
        class_type (Union[Unset, str]):
        class_value (Union[Unset, str]):
        dependent (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        payor (Union[Unset, str]):
        policy_holder (Union[Unset, str]):
        status (Union[Unset, str]):
        subscriber (Union[Unset, str]):
        type_ (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        beneficiary=beneficiary,
        class_type=class_type,
        class_value=class_value,
        dependent=dependent,
        identifier=identifier,
        patient=patient,
        payor=payor,
        policy_holder=policy_holder,
        status=status,
        subscriber=subscriber,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
