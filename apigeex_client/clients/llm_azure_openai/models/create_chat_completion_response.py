from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage
    from ..models.create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
    from ..models.prompt_filter_result import PromptFilterResult


T = TypeVar("T", bound="CreateChatCompletionResponse")


@_attrs_define
class CreateChatCompletionResponse:
    """
    Attributes:
        id (str):
        object_ (str):
        created (int):
        model (str):
        choices (list['CreateChatCompletionResponseChoicesItem']):
        usage (Union[Unset, ChatCompletionsResponseCommonUsage]):
        prompt_filter_results (Union[Unset, list['PromptFilterResult']]): Content filtering results for zero or more
            prompts in the request. In a streaming request, results for different prompts may arrive at different times or
            in different orders.
    """

    id: str
    object_: str
    created: int
    model: str
    choices: list["CreateChatCompletionResponseChoicesItem"]
    usage: Union[Unset, "ChatCompletionsResponseCommonUsage"] = UNSET
    prompt_filter_results: Union[Unset, list["PromptFilterResult"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        object_ = self.object_

        created = self.created

        model = self.model

        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        usage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.usage, Unset):
            usage = self.usage.to_dict()

        prompt_filter_results: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.prompt_filter_results, Unset):
            prompt_filter_results = []
            for componentsschemasprompt_filter_results_item_data in self.prompt_filter_results:
                componentsschemasprompt_filter_results_item = componentsschemasprompt_filter_results_item_data.to_dict()
                prompt_filter_results.append(componentsschemasprompt_filter_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created": created,
                "model": model,
                "choices": choices,
            }
        )
        if usage is not UNSET:
            field_dict["usage"] = usage
        if prompt_filter_results is not UNSET:
            field_dict["prompt_filter_results"] = prompt_filter_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completions_response_common_usage import ChatCompletionsResponseCommonUsage
        from ..models.create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
        from ..models.prompt_filter_result import PromptFilterResult

        d = dict(src_dict)
        id = d.pop("id")

        object_ = d.pop("object")

        created = d.pop("created")

        model = d.pop("model")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = CreateChatCompletionResponseChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        _usage = d.pop("usage", UNSET)
        usage: Union[Unset, ChatCompletionsResponseCommonUsage]
        if isinstance(_usage, Unset):
            usage = UNSET
        else:
            usage = ChatCompletionsResponseCommonUsage.from_dict(_usage)

        prompt_filter_results = []
        _prompt_filter_results = d.pop("prompt_filter_results", UNSET)
        for componentsschemasprompt_filter_results_item_data in _prompt_filter_results or []:
            componentsschemasprompt_filter_results_item = PromptFilterResult.from_dict(
                componentsschemasprompt_filter_results_item_data
            )

            prompt_filter_results.append(componentsschemasprompt_filter_results_item)

        create_chat_completion_response = cls(
            id=id,
            object_=object_,
            created=created,
            model=model,
            choices=choices,
            usage=usage,
            prompt_filter_results=prompt_filter_results,
        )

        create_chat_completion_response.additional_properties = d
        return create_chat_completion_response

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
