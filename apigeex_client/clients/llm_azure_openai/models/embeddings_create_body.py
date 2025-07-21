from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmbeddingsCreateBody")


@_attrs_define
class EmbeddingsCreateBody:
    r"""
    Attributes:
        input_ (Union[None, list[str], str]): Input text to get embeddings for, encoded as a string. To get embeddings
            for multiple inputs in a single request, pass an array of strings. Each input must not exceed 2048 tokens in
            length.
            Unless you are embedding code, we suggest replacing newlines (\n) in your input with a single space, as we have
            observed inferior results when newlines are present.
        user (Union[Unset, str]): A unique identifier representing your end-user, which can help monitoring and
            detecting abuse.
        input_type (Union[Unset, str]): input type of embedding search to use Example: query.
    """

    input_: Union[None, list[str], str]
    user: Union[Unset, str] = UNSET
    input_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_: Union[None, list[str], str]
        if isinstance(self.input_, list):
            input_ = self.input_

        else:
            input_ = self.input_

        user = self.user

        input_type = self.input_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "input": input_,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user
        if input_type is not UNSET:
            field_dict["input_type"] = input_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_input_(data: object) -> Union[None, list[str], str]:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                input_type_1 = cast(list[str], data)

                return input_type_1
            except:  # noqa: E722
                pass
            return cast(Union[None, list[str], str], data)

        input_ = _parse_input_(d.pop("input"))

        user = d.pop("user", UNSET)

        input_type = d.pop("input_type", UNSET)

        embeddings_create_body = cls(
            input_=input_,
            user=user,
            input_type=input_type,
        )

        embeddings_create_body.additional_properties = d
        return embeddings_create_body

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
