from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_filter_result_severity import ContentFilterResultSeverity

T = TypeVar("T", bound="ContentFilterResult")


@_attrs_define
class ContentFilterResult:
    """
    Attributes:
        severity (ContentFilterResultSeverity):
        filtered (bool):
    """

    severity: ContentFilterResultSeverity
    filtered: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        severity = self.severity.value

        filtered = self.filtered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "severity": severity,
                "filtered": filtered,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        severity = ContentFilterResultSeverity(d.pop("severity"))

        filtered = d.pop("filtered")

        content_filter_result = cls(
            severity=severity,
            filtered=filtered,
        )

        content_filter_result.additional_properties = d
        return content_filter_result

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
