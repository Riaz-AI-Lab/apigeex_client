from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage


T = TypeVar("T", bound="ChatCompletionsResponseCommon")


@_attrs_define
class ChatCompletionsResponseCommon:
    """
    Attributes:
        id (str):
        object_ (str):
        created (int):
        model (str):
        usage (Union[Unset, ChatCompletionsResponseCommonUsage]):
    """

    id: str
    object_: str
    created: int
    model: str
    usage: Union[Unset, "ChatCompletionsResponseCommonUsage"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        created = self.created

        model = self.model

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created": created,
                "model": model,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage

        d = dict(src_dict)
        id = d.pop("id")

        object_ = d.pop("object")

        created = d.pop("created")

        model = d.pop("model")

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ChatCompletionsResponseCommonUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ChatCompletionsResponseCommonUsage.from_dict(_usage)

        chat_completions_response_common = cls(
            id=id,
            object_=object_,
            created=created,
            model=model,
            usage=usage,
        )

        chat_completions_response_common.additional_properties = d
        return chat_completions_response_common

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
