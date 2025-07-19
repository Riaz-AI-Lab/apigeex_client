from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.embeddings_create_response_200_data_item import EmbeddingsCreateResponse200DataItem
    from ..models.embeddings_create_response_200_usage import EmbeddingsCreateResponse200Usage


T = TypeVar("T", bound="EmbeddingsCreateResponse200")


@_attrs_define
class EmbeddingsCreateResponse200:
    """
    Attributes:
        object_ (str):
        model (str):
        data (list['EmbeddingsCreateResponse200DataItem']):
        usage (EmbeddingsCreateResponse200Usage):
    """

    object_: str
    model: str
    data: list["EmbeddingsCreateResponse200DataItem"]
    usage: "EmbeddingsCreateResponse200Usage"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_

        model = self.model

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "model": model,
                "data": data,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embeddings_create_response_200_data_item import EmbeddingsCreateResponse200DataItem
        from ..models.embeddings_create_response_200_usage import EmbeddingsCreateResponse200Usage

        d = dict(src_dict)
        object_ = d.pop("object")

        model = d.pop("model")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = EmbeddingsCreateResponse200DataItem.from_dict(data_item_data)

            data.append(data_item)

        usage = EmbeddingsCreateResponse200Usage.from_dict(d.pop("usage"))

        embeddings_create_response_200 = cls(
            object_=object_,
            model=model,
            data=data,
            usage=usage,
        )

        embeddings_create_response_200.additional_properties = d
        return embeddings_create_response_200

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
