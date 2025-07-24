from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    code: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    combo_code: Union[Unset, str] = UNSET,
    combo_data_absent_reason: Union[Unset, str] = UNSET,
    combo_value_concept: Union[Unset, str] = UNSET,
    combo_value_quantity: Union[Unset, str] = UNSET,
    component_code: Union[Unset, str] = UNSET,
    component_data_absent_reason: Union[Unset, str] = UNSET,
    component_value_concept: Union[Unset, str] = UNSET,
    component_value_quantity: Union[Unset, str] = UNSET,
    data_absent_reason: Union[Unset, str] = UNSET,
    derived_from: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    focus: Union[Unset, str] = UNSET,
    has_member: Union[Unset, str] = UNSET,
    method: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    value_concept: Union[Unset, str] = UNSET,
    value_date: Union[Unset, str] = UNSET,
    value_quantity: Union[Unset, str] = UNSET,
    value_string: Union[Unset, str] = UNSET,
    code_value_concept: Union[Unset, str] = UNSET,
    code_value_date: Union[Unset, str] = UNSET,
    code_value_quantity: Union[Unset, str] = UNSET,
    code_value_string: Union[Unset, str] = UNSET,
    combo_code_value_concept: Union[Unset, str] = UNSET,
    combo_code_value_quantity: Union[Unset, str] = UNSET,
    component_code_value_concept: Union[Unset, str] = UNSET,
    component_code_value_quantity: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["date"] = date

    params["identifier"] = identifier

    params["patient"] = patient

    params["encounter"] = encounter

    params["based-on"] = based_on

    params["category"] = category

    params["combo-code"] = combo_code

    params["combo-data-absent-reason"] = combo_data_absent_reason

    params["combo-value-concept"] = combo_value_concept

    params["combo-value-quantity"] = combo_value_quantity

    params["component-code"] = component_code

    params["component-data-absent-reason"] = component_data_absent_reason

    params["component-value-concept"] = component_value_concept

    params["component-value-quantity"] = component_value_quantity

    params["data-absent-reason"] = data_absent_reason

    params["derived-from"] = derived_from

    params["device"] = device

    params["focus"] = focus

    params["has-member"] = has_member

    params["method"] = method

    params["part-of"] = part_of

    params["performer"] = performer

    params["specimen"] = specimen

    params["status"] = status

    params["subject"] = subject

    params["value-concept"] = value_concept

    params["value-date"] = value_date

    params["value-quantity"] = value_quantity

    params["value-string"] = value_string

    params["code-value-concept"] = code_value_concept

    params["code-value-date"] = code_value_date

    params["code-value-quantity"] = code_value_quantity

    params["code-value-string"] = code_value_string

    params["combo-code-value-concept"] = combo_code_value_concept

    params["combo-code-value-quantity"] = combo_code_value_quantity

    params["component-code-value-concept"] = component_code_value_concept

    params["component-code-value-quantity"] = component_code_value_quantity

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Observation",
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
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    combo_code: Union[Unset, str] = UNSET,
    combo_data_absent_reason: Union[Unset, str] = UNSET,
    combo_value_concept: Union[Unset, str] = UNSET,
    combo_value_quantity: Union[Unset, str] = UNSET,
    component_code: Union[Unset, str] = UNSET,
    component_data_absent_reason: Union[Unset, str] = UNSET,
    component_value_concept: Union[Unset, str] = UNSET,
    component_value_quantity: Union[Unset, str] = UNSET,
    data_absent_reason: Union[Unset, str] = UNSET,
    derived_from: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    focus: Union[Unset, str] = UNSET,
    has_member: Union[Unset, str] = UNSET,
    method: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    value_concept: Union[Unset, str] = UNSET,
    value_date: Union[Unset, str] = UNSET,
    value_quantity: Union[Unset, str] = UNSET,
    value_string: Union[Unset, str] = UNSET,
    code_value_concept: Union[Unset, str] = UNSET,
    code_value_date: Union[Unset, str] = UNSET,
    code_value_quantity: Union[Unset, str] = UNSET,
    code_value_string: Union[Unset, str] = UNSET,
    combo_code_value_concept: Union[Unset, str] = UNSET,
    combo_code_value_quantity: Union[Unset, str] = UNSET,
    component_code_value_concept: Union[Unset, str] = UNSET,
    component_code_value_quantity: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        encounter (Union[Unset, str]):
        based_on (Union[Unset, str]):
        category (Union[Unset, str]):
        combo_code (Union[Unset, str]):
        combo_data_absent_reason (Union[Unset, str]):
        combo_value_concept (Union[Unset, str]):
        combo_value_quantity (Union[Unset, str]):
        component_code (Union[Unset, str]):
        component_data_absent_reason (Union[Unset, str]):
        component_value_concept (Union[Unset, str]):
        component_value_quantity (Union[Unset, str]):
        data_absent_reason (Union[Unset, str]):
        derived_from (Union[Unset, str]):
        device (Union[Unset, str]):
        focus (Union[Unset, str]):
        has_member (Union[Unset, str]):
        method (Union[Unset, str]):
        part_of (Union[Unset, str]):
        performer (Union[Unset, str]):
        specimen (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):
        value_concept (Union[Unset, str]):
        value_date (Union[Unset, str]):
        value_quantity (Union[Unset, str]):
        value_string (Union[Unset, str]):
        code_value_concept (Union[Unset, str]):
        code_value_date (Union[Unset, str]):
        code_value_quantity (Union[Unset, str]):
        code_value_string (Union[Unset, str]):
        combo_code_value_concept (Union[Unset, str]):
        combo_code_value_quantity (Union[Unset, str]):
        component_code_value_concept (Union[Unset, str]):
        component_code_value_quantity (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        date=date,
        identifier=identifier,
        patient=patient,
        encounter=encounter,
        based_on=based_on,
        category=category,
        combo_code=combo_code,
        combo_data_absent_reason=combo_data_absent_reason,
        combo_value_concept=combo_value_concept,
        combo_value_quantity=combo_value_quantity,
        component_code=component_code,
        component_data_absent_reason=component_data_absent_reason,
        component_value_concept=component_value_concept,
        component_value_quantity=component_value_quantity,
        data_absent_reason=data_absent_reason,
        derived_from=derived_from,
        device=device,
        focus=focus,
        has_member=has_member,
        method=method,
        part_of=part_of,
        performer=performer,
        specimen=specimen,
        status=status,
        subject=subject,
        value_concept=value_concept,
        value_date=value_date,
        value_quantity=value_quantity,
        value_string=value_string,
        code_value_concept=code_value_concept,
        code_value_date=code_value_date,
        code_value_quantity=code_value_quantity,
        code_value_string=code_value_string,
        combo_code_value_concept=combo_code_value_concept,
        combo_code_value_quantity=combo_code_value_quantity,
        component_code_value_concept=component_code_value_concept,
        component_code_value_quantity=component_code_value_quantity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    code: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    combo_code: Union[Unset, str] = UNSET,
    combo_data_absent_reason: Union[Unset, str] = UNSET,
    combo_value_concept: Union[Unset, str] = UNSET,
    combo_value_quantity: Union[Unset, str] = UNSET,
    component_code: Union[Unset, str] = UNSET,
    component_data_absent_reason: Union[Unset, str] = UNSET,
    component_value_concept: Union[Unset, str] = UNSET,
    component_value_quantity: Union[Unset, str] = UNSET,
    data_absent_reason: Union[Unset, str] = UNSET,
    derived_from: Union[Unset, str] = UNSET,
    device: Union[Unset, str] = UNSET,
    focus: Union[Unset, str] = UNSET,
    has_member: Union[Unset, str] = UNSET,
    method: Union[Unset, str] = UNSET,
    part_of: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
    value_concept: Union[Unset, str] = UNSET,
    value_date: Union[Unset, str] = UNSET,
    value_quantity: Union[Unset, str] = UNSET,
    value_string: Union[Unset, str] = UNSET,
    code_value_concept: Union[Unset, str] = UNSET,
    code_value_date: Union[Unset, str] = UNSET,
    code_value_quantity: Union[Unset, str] = UNSET,
    code_value_string: Union[Unset, str] = UNSET,
    combo_code_value_concept: Union[Unset, str] = UNSET,
    combo_code_value_quantity: Union[Unset, str] = UNSET,
    component_code_value_concept: Union[Unset, str] = UNSET,
    component_code_value_quantity: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        code (Union[Unset, str]):
        date (Union[Unset, str]):
        identifier (Union[Unset, str]):
        patient (Union[Unset, str]):
        encounter (Union[Unset, str]):
        based_on (Union[Unset, str]):
        category (Union[Unset, str]):
        combo_code (Union[Unset, str]):
        combo_data_absent_reason (Union[Unset, str]):
        combo_value_concept (Union[Unset, str]):
        combo_value_quantity (Union[Unset, str]):
        component_code (Union[Unset, str]):
        component_data_absent_reason (Union[Unset, str]):
        component_value_concept (Union[Unset, str]):
        component_value_quantity (Union[Unset, str]):
        data_absent_reason (Union[Unset, str]):
        derived_from (Union[Unset, str]):
        device (Union[Unset, str]):
        focus (Union[Unset, str]):
        has_member (Union[Unset, str]):
        method (Union[Unset, str]):
        part_of (Union[Unset, str]):
        performer (Union[Unset, str]):
        specimen (Union[Unset, str]):
        status (Union[Unset, str]):
        subject (Union[Unset, str]):
        value_concept (Union[Unset, str]):
        value_date (Union[Unset, str]):
        value_quantity (Union[Unset, str]):
        value_string (Union[Unset, str]):
        code_value_concept (Union[Unset, str]):
        code_value_date (Union[Unset, str]):
        code_value_quantity (Union[Unset, str]):
        code_value_string (Union[Unset, str]):
        combo_code_value_concept (Union[Unset, str]):
        combo_code_value_quantity (Union[Unset, str]):
        component_code_value_concept (Union[Unset, str]):
        component_code_value_quantity (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        code=code,
        date=date,
        identifier=identifier,
        patient=patient,
        encounter=encounter,
        based_on=based_on,
        category=category,
        combo_code=combo_code,
        combo_data_absent_reason=combo_data_absent_reason,
        combo_value_concept=combo_value_concept,
        combo_value_quantity=combo_value_quantity,
        component_code=component_code,
        component_data_absent_reason=component_data_absent_reason,
        component_value_concept=component_value_concept,
        component_value_quantity=component_value_quantity,
        data_absent_reason=data_absent_reason,
        derived_from=derived_from,
        device=device,
        focus=focus,
        has_member=has_member,
        method=method,
        part_of=part_of,
        performer=performer,
        specimen=specimen,
        status=status,
        subject=subject,
        value_concept=value_concept,
        value_date=value_date,
        value_quantity=value_quantity,
        value_string=value_string,
        code_value_concept=code_value_concept,
        code_value_date=code_value_date,
        code_value_quantity=code_value_quantity,
        code_value_string=code_value_string,
        combo_code_value_concept=combo_code_value_concept,
        combo_code_value_quantity=combo_code_value_quantity,
        component_code_value_concept=component_code_value_concept,
        component_code_value_quantity=component_code_value_quantity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
