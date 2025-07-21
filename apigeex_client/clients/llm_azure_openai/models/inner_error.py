from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.inner_error_code import InnerErrorCode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_filter_results import ContentFilterResults


T = TypeVar("T", bound="InnerError")


@_attrs_define
class InnerError:
    """Inner error with additional details.

    Attributes:
        code (Union[Unset, InnerErrorCode]): Error codes for the inner error object.
        content_filter_results (Union[Unset, ContentFilterResults]): Information about the content filtering category
            (hate, sexual, violence, self_harm), if it has been detected, as well as the severity level (very_low, low,
            medium, high-scale that determines the intensity and risk level of harmful content) and if it has been filtered
            or not.
    """

    code: Union[Unset, InnerErrorCode] = UNSET
    content_filter_results: Union[Unset, "ContentFilterResults"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        content_filter_results: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content_filter_results, Unset):
            content_filter_results = self.content_filter_results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if content_filter_results is not UNSET:
            field_dict["content_filter_results"] = content_filter_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_filter_results import ContentFilterResults

        d = dict(src_dict)
        _code = d.pop("code", UNSET)
        code: Union[Unset, InnerErrorCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = InnerErrorCode(_code)

        _content_filter_results = d.pop("content_filter_results", UNSET)
        content_filter_results: Union[Unset, ContentFilterResults]
        if isinstance(_content_filter_results, Unset):
            content_filter_results = UNSET
        else:
            content_filter_results = ContentFilterResults.from_dict(_content_filter_results)

        inner_error = cls(
            code=code,
            content_filter_results=content_filter_results,
        )

        inner_error.additional_properties = d
        return inner_error

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
