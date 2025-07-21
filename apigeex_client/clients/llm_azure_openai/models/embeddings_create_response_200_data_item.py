from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EmbeddingsCreateResponse200DataItem")


@_attrs_define
class EmbeddingsCreateResponse200DataItem:
    """
    Attributes:
        index (int):
        object_ (str):
        embedding (list[float]):
    """

    index: int
    object_: str
    embedding: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        object_ = self.object_

        embedding = self.embedding

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index": index,
                "object": object_,
                "embedding": embedding,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        index = d.pop("index")

        object_ = d.pop("object")

        embedding = cast(list[float], d.pop("embedding"))

        embeddings_create_response_200_data_item = cls(
            index=index,
            object_=object_,
            embedding=embedding,
        )

        embeddings_create_response_200_data_item.additional_properties = d
        return embeddings_create_response_200_data_item

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
