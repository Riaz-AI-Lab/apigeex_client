from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_filter_result import ContentFilterResult
    from ..models.error_base import ErrorBase


T = TypeVar("T", bound="ContentFilterResults")


@_attrs_define
class ContentFilterResults:
    """Information about the content filtering category (hate, sexual, violence, self_harm), if it has been detected, as
    well as the severity level (very_low, low, medium, high-scale that determines the intensity and risk level of
    harmful content) and if it has been filtered or not.

        Attributes:
            sexual (Union[Unset, ContentFilterResult]):
            violence (Union[Unset, ContentFilterResult]):
            hate (Union[Unset, ContentFilterResult]):
            self_harm (Union[Unset, ContentFilterResult]):
            error (Union[Unset, ErrorBase]):
    """

    sexual: Union[Unset, "ContentFilterResult"] = UNSET
    violence: Union[Unset, "ContentFilterResult"] = UNSET
    hate: Union[Unset, "ContentFilterResult"] = UNSET
    self_harm: Union[Unset, "ContentFilterResult"] = UNSET
    error: Union[Unset, "ErrorBase"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sexual: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sexual, Unset):
            sexual = self.sexual.to_dict()

        violence: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.violence, Unset):
            violence = self.violence.to_dict()

        hate: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.hate, Unset):
            hate = self.hate.to_dict()

        self_harm: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.self_harm, Unset):
            self_harm = self.self_harm.to_dict()

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sexual is not UNSET:
            field_dict["sexual"] = sexual
        if violence is not UNSET:
            field_dict["violence"] = violence
        if hate is not UNSET:
            field_dict["hate"] = hate
        if self_harm is not UNSET:
            field_dict["self_harm"] = self_harm
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_filter_result import ContentFilterResult
        from ..models.error_base import ErrorBase

        d = dict(src_dict)
        _sexual = d.pop("sexual", UNSET)
        sexual: Union[Unset, ContentFilterResult]
        if isinstance(_sexual, Unset):
            sexual = UNSET
        else:
            sexual = ContentFilterResult.from_dict(_sexual)

        _violence = d.pop("violence", UNSET)
        violence: Union[Unset, ContentFilterResult]
        if isinstance(_violence, Unset):
            violence = UNSET
        else:
            violence = ContentFilterResult.from_dict(_violence)

        _hate = d.pop("hate", UNSET)
        hate: Union[Unset, ContentFilterResult]
        if isinstance(_hate, Unset):
            hate = UNSET
        else:
            hate = ContentFilterResult.from_dict(_hate)

        _self_harm = d.pop("self_harm", UNSET)
        self_harm: Union[Unset, ContentFilterResult]
        if isinstance(_self_harm, Unset):
            self_harm = UNSET
        else:
            self_harm = ContentFilterResult.from_dict(_self_harm)

        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorBase]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorBase.from_dict(_error)

        content_filter_results = cls(
            sexual=sexual,
            violence=violence,
            hate=hate,
            self_harm=self_harm,
            error=error,
        )

        content_filter_results.additional_properties = d
        return content_filter_results

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
