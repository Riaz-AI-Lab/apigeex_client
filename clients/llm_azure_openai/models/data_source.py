from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_source_parameters import DataSourceParameters


T = TypeVar("T", bound="DataSource")


@_attrs_define
class DataSource:
    """The data source to be used for the Azure OpenAI on your data feature.

    Attributes:
        type_ (str): The data source type.
        parameters (Union[Unset, DataSourceParameters]): The parameters to be used for the data source in runtime.
    """

    type_: str
    parameters: Union[Unset, "DataSourceParameters"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_source_parameters import DataSourceParameters

        d = dict(src_dict)
        type_ = d.pop("type")

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, DataSourceParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = DataSourceParameters.from_dict(_parameters)

        data_source = cls(
            type_=type_,
            parameters=parameters,
        )

        data_source.additional_properties = d
        return data_source

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
