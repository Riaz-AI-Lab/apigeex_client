from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SearchRequestType0")


@_attrs_define
class SearchRequestType0:
    """Refer to the [search](https://cloud.google.com/generative-ai-app-
    builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search) api reference for supported
    attributes

        Example:
            {'query': 'Some example query', 'pageSize': 10, 'queryExpansionSpec': {'condition': 'AUTO'},
                'spellCorrectionSpec': {'mode': 'AUTO'}, 'contentSearchSpec': {'summarySpec': {'summaryResultCount': 5,
                'ignoreAdversarialQuery': True, 'includeCitations': True}, 'snippetSpec': {'returnSnippet': True},
                'extractiveContentSpec': {'maxExtractiveAnswerCount': 1}}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search_request_type_0 = cls()

        search_request_type_0.additional_properties = d
        return search_request_type_0

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
