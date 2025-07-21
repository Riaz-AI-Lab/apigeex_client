from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_function_parameters import ChatCompletionFunctionParameters


T = TypeVar("T", bound="ChatCompletionFunctions")


@_attrs_define
class ChatCompletionFunctions:
    """
    Attributes:
        name (str): The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes,
            with a maximum length of 64.
        description (Union[Unset, str]): The description of what the function does.
        parameters (Union[Unset, ChatCompletionFunctionParameters]): The parameters the functions accepts, described as
            a JSON Schema object. See the [guide](/docs/guides/gpt/function-calling) for examples, and the [JSON Schema
            reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.
    """

    name: str
    description: Union[Unset, str] = UNSET
    parameters: Union[Unset, "ChatCompletionFunctionParameters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_function_parameters import ChatCompletionFunctionParameters

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ChatCompletionFunctionParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ChatCompletionFunctionParameters.from_dict(_parameters)

        chat_completion_functions = cls(
            name=name,
            description=description,
            parameters=parameters,
        )

        chat_completion_functions.additional_properties = d
        return chat_completion_functions

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
