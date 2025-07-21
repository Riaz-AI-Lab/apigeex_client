from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage
    from ..models.extensions_chat_completion_choice import ExtensionsChatCompletionChoice


T = TypeVar("T", bound="ExtensionsChatCompletionsResponse")


@_attrs_define
class ExtensionsChatCompletionsResponse:
    """The response of the extensions chat completions.

    Example:
        {'id': '1', 'object': 'extensions.chat.completion', 'created': 1679201802, 'model': 'gpt-3.5-turbo-0301',
            'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'Seattle is a
            great place for hiking! Here are some of the best hiking places in Seattle according to Contoso Traveler [doc1]
            and West Coast Traveler, Snow Lake, Mount Si, and Mount Tenerife [doc2]. I hope this helps! Let me know if you
            need more information.', 'end_turn': True, 'context': {'messages': [{'role': 'tool', 'content':
            '{"citations":[{"filepath":"ContosoTraveler.pdf","content":"This is the content of the citation
            1"},{"filepath":"WestCoastTraveler.html","content":"This is the content of the citation 2"},{"content":"This is
            the content of the citation 3 without filepath"}],"intent":"hiking place in seattle"}', 'end_turn': False}]}}}]}

    Attributes:
        id (str):
        object_ (str):
        created (int):
        model (str):
        usage (Union[Unset, ChatCompletionsResponseCommonUsage]):
        choices (Union[Unset, list['ExtensionsChatCompletionChoice']]):
    """

    id: str
    object_: str
    created: int
    model: str
    usage: Union[Unset, "ChatCompletionsResponseCommonUsage"] = UNSET
    choices: Union[Unset, list["ExtensionsChatCompletionChoice"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        created = self.created

        model = self.model

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        choices: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.choices, Unset):
            choices = []
            for choices_item_data in self.choices:
                choices_item = choices_item_data.to_dict()
                choices.append(choices_item)

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
        if choices is not UNSET:
            field_dict["choices"] = choices

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage
        from ..models.extensions_chat_completion_choice import ExtensionsChatCompletionChoice

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

        choices = []
        _choices = d.pop("choices", UNSET)
        for choices_item_data in _choices or []:
            choices_item = ExtensionsChatCompletionChoice.from_dict(choices_item_data)

            choices.append(choices_item)

        extensions_chat_completions_response = cls(
            id=id,
            object_=object_,
            created=created,
            model=model,
            usage=usage,
            choices=choices,
        )

        extensions_chat_completions_response.additional_properties = d
        return extensions_chat_completions_response

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
