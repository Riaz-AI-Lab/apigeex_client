from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    context: Union[Unset, str] = UNSET,
    context_quantity: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    jurisdiction: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    dependson: Union[Unset, str] = UNSET,
    other: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_code: Union[Unset, str] = UNSET,
    source_system: Union[Unset, str] = UNSET,
    source_uri: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    target_code: Union[Unset, str] = UNSET,
    target_system: Union[Unset, str] = UNSET,
    target_uri: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["context"] = context

    params["context-quantity"] = context_quantity

    params["context-type"] = context_type

    params["date"] = date

    params["description"] = description

    params["jurisdiction"] = jurisdiction

    params["name"] = name

    params["publisher"] = publisher

    params["status"] = status

    params["title"] = title

    params["url"] = url_query

    params["version"] = version

    params["identifier"] = identifier

    params["dependson"] = dependson

    params["other"] = other

    params["product"] = product

    params["source"] = source

    params["source-code"] = source_code

    params["source-system"] = source_system

    params["source-uri"] = source_uri

    params["target"] = target

    params["target-code"] = target_code

    params["target-system"] = target_system

    params["target-uri"] = target_uri

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/ConceptMap",
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
    context: Union[Unset, str] = UNSET,
    context_quantity: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    jurisdiction: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    dependson: Union[Unset, str] = UNSET,
    other: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_code: Union[Unset, str] = UNSET,
    source_system: Union[Unset, str] = UNSET,
    source_uri: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    target_code: Union[Unset, str] = UNSET,
    target_system: Union[Unset, str] = UNSET,
    target_uri: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        context (Union[Unset, str]):
        context_quantity (Union[Unset, str]):
        context_type (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        jurisdiction (Union[Unset, str]):
        name (Union[Unset, str]):
        publisher (Union[Unset, str]):
        status (Union[Unset, str]):
        title (Union[Unset, str]):
        url_query (Union[Unset, str]):
        version (Union[Unset, str]):
        identifier (Union[Unset, str]):
        dependson (Union[Unset, str]):
        other (Union[Unset, str]):
        product (Union[Unset, str]):
        source (Union[Unset, str]):
        source_code (Union[Unset, str]):
        source_system (Union[Unset, str]):
        source_uri (Union[Unset, str]):
        target (Union[Unset, str]):
        target_code (Union[Unset, str]):
        target_system (Union[Unset, str]):
        target_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        context=context,
        context_quantity=context_quantity,
        context_type=context_type,
        date=date,
        description=description,
        jurisdiction=jurisdiction,
        name=name,
        publisher=publisher,
        status=status,
        title=title,
        url_query=url_query,
        version=version,
        identifier=identifier,
        dependson=dependson,
        other=other,
        product=product,
        source=source,
        source_code=source_code,
        source_system=source_system,
        source_uri=source_uri,
        target=target,
        target_code=target_code,
        target_system=target_system,
        target_uri=target_uri,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    context: Union[Unset, str] = UNSET,
    context_quantity: Union[Unset, str] = UNSET,
    context_type: Union[Unset, str] = UNSET,
    date: Union[Unset, str] = UNSET,
    description: Union[Unset, str] = UNSET,
    jurisdiction: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    publisher: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    url_query: Union[Unset, str] = UNSET,
    version: Union[Unset, str] = UNSET,
    identifier: Union[Unset, str] = UNSET,
    dependson: Union[Unset, str] = UNSET,
    other: Union[Unset, str] = UNSET,
    product: Union[Unset, str] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_code: Union[Unset, str] = UNSET,
    source_system: Union[Unset, str] = UNSET,
    source_uri: Union[Unset, str] = UNSET,
    target: Union[Unset, str] = UNSET,
    target_code: Union[Unset, str] = UNSET,
    target_system: Union[Unset, str] = UNSET,
    target_uri: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """Performs a search over the resources of this type based upon specified search parameters / criteria
    and returns a FHIR Bundle resource with the results.

    Args:
        context (Union[Unset, str]):
        context_quantity (Union[Unset, str]):
        context_type (Union[Unset, str]):
        date (Union[Unset, str]):
        description (Union[Unset, str]):
        jurisdiction (Union[Unset, str]):
        name (Union[Unset, str]):
        publisher (Union[Unset, str]):
        status (Union[Unset, str]):
        title (Union[Unset, str]):
        url_query (Union[Unset, str]):
        version (Union[Unset, str]):
        identifier (Union[Unset, str]):
        dependson (Union[Unset, str]):
        other (Union[Unset, str]):
        product (Union[Unset, str]):
        source (Union[Unset, str]):
        source_code (Union[Unset, str]):
        source_system (Union[Unset, str]):
        source_uri (Union[Unset, str]):
        target (Union[Unset, str]):
        target_code (Union[Unset, str]):
        target_system (Union[Unset, str]):
        target_uri (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        context=context,
        context_quantity=context_quantity,
        context_type=context_type,
        date=date,
        description=description,
        jurisdiction=jurisdiction,
        name=name,
        publisher=publisher,
        status=status,
        title=title,
        url_query=url_query,
        version=version,
        identifier=identifier,
        dependson=dependson,
        other=other,
        product=product,
        source=source,
        source_code=source_code,
        source_system=source_system,
        source_uri=source_uri,
        target=target,
        target_code=target_code,
        target_system=target_system,
        target_uri=target_uri,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
