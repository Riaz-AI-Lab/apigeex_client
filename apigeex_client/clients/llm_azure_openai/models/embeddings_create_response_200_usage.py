from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmbeddingsCreateResponse200Usage")


@_attrs_define
class EmbeddingsCreateResponse200Usage:
    """
    Attributes:
        prompt_tokens (int):
        total_tokens (int):
    """

    prompt_tokens: int
    total_tokens: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        prompt_tokens = self.prompt_tokens

        total_tokens = self.total_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        prompt_tokens = d.pop("prompt_tokens")

        total_tokens = d.pop("total_tokens")

        embeddings_create_response_200_usage = cls(
            prompt_tokens=prompt_tokens,
            total_tokens=total_tokens,
        )

        embeddings_create_response_200_usage.additional_properties = d
        return embeddings_create_response_200_usage

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
