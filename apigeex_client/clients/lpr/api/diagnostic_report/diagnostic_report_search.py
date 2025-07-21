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
    conclusion: Union[Unset, str] = UNSET,
    issued: Union[Unset, str] = UNSET,
    media: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    result: Union[Unset, str] = UNSET,
    results_interpreter: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["code"] = code

    params["date"] = date

    params["identifier"] = identifier

    params["patient"] = patient

    params["encounter"] = encounter

    params["based-on"] = based_on

    params["category"] = category

    params["conclusion"] = conclusion

    params["issued"] = issued

    params["media"] = media

    params["performer"] = performer

    params["result"] = result

    params["results-interpreter"] = results_interpreter

    params["specimen"] = specimen

    params["status"] = status

    params["subject"] = subject

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/DiagnosticReport",
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
    conclusion: Union[Unset, str] = UNSET,
    issued: Union[Unset, str] = UNSET,
    media: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    result: Union[Unset, str] = UNSET,
    results_interpreter: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
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
        conclusion (Union[Unset, str]):
        issued (Union[Unset, str]):
        media (Union[Unset, str]):
        performer (Union[Unset, str]):
        result (Union[Unset, str]):
        results_interpreter (Union[Unset, str]):
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
        date=date,
        identifier=identifier,
        patient=patient,
        encounter=encounter,
        based_on=based_on,
        category=category,
        conclusion=conclusion,
        issued=issued,
        media=media,
        performer=performer,
        result=result,
        results_interpreter=results_interpreter,
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
    date: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    patient: Union[Unset, str] = UNSET,
    encounter: Union[Unset, str] = UNSET,
    based_on: Union[Unset, str] = UNSET,
    category: Union[Unset, str] = UNSET,
    conclusion: Union[Unset, str] = UNSET,
    issued: Union[Unset, str] = UNSET,
    media: Union[Unset, str] = UNSET,
    performer: Union[Unset, str] = UNSET,
    result: Union[Unset, str] = UNSET,
    results_interpreter: Union[Unset, str] = UNSET,
    specimen: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    subject: Union[Unset, str] = UNSET,
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
        conclusion (Union[Unset, str]):
        issued (Union[Unset, str]):
        media (Union[Unset, str]):
        performer (Union[Unset, str]):
        result (Union[Unset, str]):
        results_interpreter (Union[Unset, str]):
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
        date=date,
        identifier=identifier,
        patient=patient,
        encounter=encounter,
        based_on=based_on,
        category=category,
        conclusion=conclusion,
        issued=issued,
        media=media,
        performer=performer,
        result=result,
        results_interpreter=results_interpreter,
        specimen=specimen,
        status=status,
        subject=subject,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
