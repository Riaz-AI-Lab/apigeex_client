from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_response_message import ChatCompletionResponseMessage
    from ..models.content_filter_results import ContentFilterResults


T = TypeVar("T", bound="CreateChatCompletionResponseChoicesItem")


@_attrs_define
class CreateChatCompletionResponseChoicesItem:
    """
    Attributes:
        index (Union[Unset, int]):
        finish_reason (Union[Unset, str]):
        message (Union[Unset, ChatCompletionResponseMessage]):
        content_filter_results (Union[Unset, ContentFilterResults]): Information about the content filtering category
            (hate, sexual, violence, self_harm), if it has been detected, as well as the severity level (very_low, low,
            medium, high-scale that determines the intensity and risk level of harmful content) and if it has been filtered
            or not.
    """

    index: Union[Unset, int] = UNSET
    finish_reason: Union[Unset, str] = UNSET
    message: Union[Unset, "ChatCompletionResponseMessage"] = UNSET
    content_filter_results: Union[Unset, "ContentFilterResults"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        finish_reason = self.finish_reason

        message: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.message, Unset):
            message = self.message.to_dict()

        content_filter_results: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.content_filter_results, Unset):
            content_filter_results = self.content_filter_results.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if finish_reason is not UNSET:
            field_dict["finish_reason"] = finish_reason
        if message is not UNSET:
            field_dict["message"] = message
        if content_filter_results is not UNSET:
            field_dict["content_filter_results"] = content_filter_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_response_message import ChatCompletionResponseMessage
        from ..models.content_filter_results import ContentFilterResults

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        finish_reason = d.pop("finish_reason", UNSET)

        _message = d.pop("message", UNSET)
        message: Union[Unset, ChatCompletionResponseMessage]
        if isinstance(_message, Unset):
            message = UNSET
        else:
            message = ChatCompletionResponseMessage.from_dict(_message)

        _content_filter_results = d.pop("content_filter_results", UNSET)
        content_filter_results: Union[Unset, ContentFilterResults]
        if isinstance(_content_filter_results, Unset):
            content_filter_results = UNSET
        else:
            content_filter_results = ContentFilterResults.from_dict(_content_filter_results)

        create_chat_completion_response_choices_item = cls(
            index=index,
            finish_reason=finish_reason,
            message=message,
            content_filter_results=content_filter_results,
        )

        create_chat_completion_response_choices_item.additional_properties = d
        return create_chat_completion_response_choices_item

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
