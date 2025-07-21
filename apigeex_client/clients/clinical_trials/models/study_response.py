from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.study_resource import StudyResource


T = TypeVar("T", bound="StudyResponse")


@_attrs_define
class StudyResponse:
    """
    Attributes:
        study (Union['StudyResource', list['StudyResource']]):
    """

    study: Union["StudyResource", list["StudyResource"]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.study_resource import StudyResource

        study: Union[dict[str, Any], list[dict[str, Any]]]
        if isinstance(self.study, StudyResource):
            study = self.study.to_dict()
        else:
            study = []
            for study_type_1_item_data in self.study:
                study_type_1_item = study_type_1_item_data.to_dict()
                study.append(study_type_1_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "study": study,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.study_resource import StudyResource

        d = dict(src_dict)

        def _parse_study(data: object) -> Union["StudyResource", list["StudyResource"]]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                study_type_0 = StudyResource.from_dict(data)

                return study_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            study_type_1 = []
            _study_type_1 = data
            for study_type_1_item_data in _study_type_1:
                study_type_1_item = StudyResource.from_dict(study_type_1_item_data)

                study_type_1.append(study_type_1_item)

            return study_type_1

        study = _parse_study(d.pop("study"))

        study_response = cls(
            study=study,
        )

        study_response.additional_properties = d
        return study_response

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
