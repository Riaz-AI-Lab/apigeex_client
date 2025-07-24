from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SessionsRequestType0")


@_attrs_define
class SessionsRequestType0:
    """Refer to the [Sessions](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1alpha/projects.locations.dataStores.sessions#Sessions) api reference for supported
    attributes

        Example:
            {'query': {'name': 'session name', 'userPseudoId': 'A unique identifier for tracking users'}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sessions_request_type_0 = cls()

        sessions_request_type_0.additional_properties = d
        return sessions_request_type_0

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
