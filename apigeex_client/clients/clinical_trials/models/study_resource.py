import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.study_resource_site_summary_json_type_0_item import StudyResourceSiteSummaryJSONType0Item
    from ..models.study_resource_study_metadata_json_type_0 import StudyResourceStudyMetadataJsonType0


T = TypeVar("T", bound="StudyResource")


@_attrs_define
class StudyResource:
    """
    Attributes:
        pk_study (int):
        contact_modified_date (Union[None, Unset, datetime.datetime]):
        current_study_status (Union[None, Unset, str]):
        eligibility_criteria (Union[None, Unset, str]):
        latest_modified_date (Union[None, Unset, datetime.datetime]):
        metadata_added_date (Union[None, Unset, datetime.datetime]):
        metadata_last_modified_date (Union[None, Unset, datetime.datetime]):
        pi_modified_date (Union[None, Unset, datetime.datetime]):
        poc_id (Union[None, Unset, str]):
        publish_state (Union[None, Unset, str]):
        row_loaded_date (Union[None, Unset, datetime.datetime]):
        site_summary_json (Union[None, Unset, list['StudyResourceSiteSummaryJSONType0Item']]):
        sponsor_protocol_id (Union[None, Unset, str]):
        status_modified_date (Union[None, Unset, datetime.datetime]):
        study_metadata_json (Union['StudyResourceStudyMetadataJsonType0', None, Unset]):
        ec_last_modified_date (Union[None, Unset, datetime.datetime]):
        irb_protocol_id (Union[None, Unset, str]):
        nct_number (Union[None, Unset, str]):
        public_modified_data (Union[None, Unset, datetime.datetime]):
        record_modified_date (Union[None, Unset, datetime.datetime]):
        sitecore_start_date (Union[None, Unset, datetime.datetime]):
        study_number (Union[None, Unset, str]):
        unpub_start_date (Union[None, Unset, datetime.datetime]):
    """

    pk_study: int
    contact_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    current_study_status: Union[None, Unset, str] = UNSET
    eligibility_criteria: Union[None, Unset, str] = UNSET
    latest_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    metadata_added_date: Union[None, Unset, datetime.datetime] = UNSET
    metadata_last_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    pi_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    poc_id: Union[None, Unset, str] = UNSET
    publish_state: Union[None, Unset, str] = UNSET
    row_loaded_date: Union[None, Unset, datetime.datetime] = UNSET
    site_summary_json: Union[None, Unset, list["StudyResourceSiteSummaryJSONType0Item"]] = UNSET
    sponsor_protocol_id: Union[None, Unset, str] = UNSET
    status_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    study_metadata_json: Union["StudyResourceStudyMetadataJsonType0", None, Unset] = UNSET
    ec_last_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    irb_protocol_id: Union[None, Unset, str] = UNSET
    nct_number: Union[None, Unset, str] = UNSET
    public_modified_data: Union[None, Unset, datetime.datetime] = UNSET
    record_modified_date: Union[None, Unset, datetime.datetime] = UNSET
    sitecore_start_date: Union[None, Unset, datetime.datetime] = UNSET
    study_number: Union[None, Unset, str] = UNSET
    unpub_start_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.study_resource_study_metadata_json_type_0 import StudyResourceStudyMetadataJsonType0

        pk_study = self.pk_study

        contact_modified_date: Union[None, Unset, str]
        if isinstance(self.contact_modified_date, Unset):
            contact_modified_date = UNSET
        elif isinstance(self.contact_modified_date, datetime.datetime):
            contact_modified_date = self.contact_modified_date.isoformat()
        else:
            contact_modified_date = self.contact_modified_date

        current_study_status: Union[None, Unset, str]
        if isinstance(self.current_study_status, Unset):
            current_study_status = UNSET
        else:
            current_study_status = self.current_study_status

        eligibility_criteria: Union[None, Unset, str]
        if isinstance(self.eligibility_criteria, Unset):
            eligibility_criteria = UNSET
        else:
            eligibility_criteria = self.eligibility_criteria

        latest_modified_date: Union[None, Unset, str]
        if isinstance(self.latest_modified_date, Unset):
            latest_modified_date = UNSET
        elif isinstance(self.latest_modified_date, datetime.datetime):
            latest_modified_date = self.latest_modified_date.isoformat()
        else:
            latest_modified_date = self.latest_modified_date

        metadata_added_date: Union[None, Unset, str]
        if isinstance(self.metadata_added_date, Unset):
            metadata_added_date = UNSET
        elif isinstance(self.metadata_added_date, datetime.datetime):
            metadata_added_date = self.metadata_added_date.isoformat()
        else:
            metadata_added_date = self.metadata_added_date

        metadata_last_modified_date: Union[None, Unset, str]
        if isinstance(self.metadata_last_modified_date, Unset):
            metadata_last_modified_date = UNSET
        elif isinstance(self.metadata_last_modified_date, datetime.datetime):
            metadata_last_modified_date = self.metadata_last_modified_date.isoformat()
        else:
            metadata_last_modified_date = self.metadata_last_modified_date

        pi_modified_date: Union[None, Unset, str]
        if isinstance(self.pi_modified_date, Unset):
            pi_modified_date = UNSET
        elif isinstance(self.pi_modified_date, datetime.datetime):
            pi_modified_date = self.pi_modified_date.isoformat()
        else:
            pi_modified_date = self.pi_modified_date

        poc_id: Union[None, Unset, str]
        if isinstance(self.poc_id, Unset):
            poc_id = UNSET
        else:
            poc_id = self.poc_id

        publish_state: Union[None, Unset, str]
        if isinstance(self.publish_state, Unset):
            publish_state = UNSET
        else:
            publish_state = self.publish_state

        row_loaded_date: Union[None, Unset, str]
        if isinstance(self.row_loaded_date, Unset):
            row_loaded_date = UNSET
        elif isinstance(self.row_loaded_date, datetime.datetime):
            row_loaded_date = self.row_loaded_date.isoformat()
        else:
            row_loaded_date = self.row_loaded_date

        site_summary_json: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.site_summary_json, Unset):
            site_summary_json = UNSET
        elif isinstance(self.site_summary_json, list):
            site_summary_json = []
            for site_summary_json_type_0_item_data in self.site_summary_json:
                site_summary_json_type_0_item = site_summary_json_type_0_item_data.to_dict()
                site_summary_json.append(site_summary_json_type_0_item)

        else:
            site_summary_json = self.site_summary_json

        sponsor_protocol_id: Union[None, Unset, str]
        if isinstance(self.sponsor_protocol_id, Unset):
            sponsor_protocol_id = UNSET
        else:
            sponsor_protocol_id = self.sponsor_protocol_id

        status_modified_date: Union[None, Unset, str]
        if isinstance(self.status_modified_date, Unset):
            status_modified_date = UNSET
        elif isinstance(self.status_modified_date, datetime.datetime):
            status_modified_date = self.status_modified_date.isoformat()
        else:
            status_modified_date = self.status_modified_date

        study_metadata_json: Union[None, Unset, dict[str, Any]]
        if isinstance(self.study_metadata_json, Unset):
            study_metadata_json = UNSET
        elif isinstance(self.study_metadata_json, StudyResourceStudyMetadataJsonType0):
            study_metadata_json = self.study_metadata_json.to_dict()
        else:
            study_metadata_json = self.study_metadata_json

        ec_last_modified_date: Union[None, Unset, str]
        if isinstance(self.ec_last_modified_date, Unset):
            ec_last_modified_date = UNSET
        elif isinstance(self.ec_last_modified_date, datetime.datetime):
            ec_last_modified_date = self.ec_last_modified_date.isoformat()
        else:
            ec_last_modified_date = self.ec_last_modified_date

        irb_protocol_id: Union[None, Unset, str]
        if isinstance(self.irb_protocol_id, Unset):
            irb_protocol_id = UNSET
        else:
            irb_protocol_id = self.irb_protocol_id

        nct_number: Union[None, Unset, str]
        if isinstance(self.nct_number, Unset):
            nct_number = UNSET
        else:
            nct_number = self.nct_number

        public_modified_data: Union[None, Unset, str]
        if isinstance(self.public_modified_data, Unset):
            public_modified_data = UNSET
        elif isinstance(self.public_modified_data, datetime.datetime):
            public_modified_data = self.public_modified_data.isoformat()
        else:
            public_modified_data = self.public_modified_data

        record_modified_date: Union[None, Unset, str]
        if isinstance(self.record_modified_date, Unset):
            record_modified_date = UNSET
        elif isinstance(self.record_modified_date, datetime.datetime):
            record_modified_date = self.record_modified_date.isoformat()
        else:
            record_modified_date = self.record_modified_date

        sitecore_start_date: Union[None, Unset, str]
        if isinstance(self.sitecore_start_date, Unset):
            sitecore_start_date = UNSET
        elif isinstance(self.sitecore_start_date, datetime.datetime):
            sitecore_start_date = self.sitecore_start_date.isoformat()
        else:
            sitecore_start_date = self.sitecore_start_date

        study_number: Union[None, Unset, str]
        if isinstance(self.study_number, Unset):
            study_number = UNSET
        else:
            study_number = self.study_number

        unpub_start_date: Union[None, Unset, str]
        if isinstance(self.unpub_start_date, Unset):
            unpub_start_date = UNSET
        elif isinstance(self.unpub_start_date, datetime.datetime):
            unpub_start_date = self.unpub_start_date.isoformat()
        else:
            unpub_start_date = self.unpub_start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pk_study": pk_study,
            }
        )
        if contact_modified_date is not UNSET:
            field_dict["Contact_Modified_Date"] = contact_modified_date
        if current_study_status is not UNSET:
            field_dict["Current_Study_Status"] = current_study_status
        if eligibility_criteria is not UNSET:
            field_dict["Eligibility_Criteria"] = eligibility_criteria
        if latest_modified_date is not UNSET:
            field_dict["Latest_Modified_Date"] = latest_modified_date
        if metadata_added_date is not UNSET:
            field_dict["Metadata_Added_Date"] = metadata_added_date
        if metadata_last_modified_date is not UNSET:
            field_dict["Metadata_Last_Modified_Date"] = metadata_last_modified_date
        if pi_modified_date is not UNSET:
            field_dict["PI_Modified_Date"] = pi_modified_date
        if poc_id is not UNSET:
            field_dict["POC_ID"] = poc_id
        if publish_state is not UNSET:
            field_dict["Publish_State"] = publish_state
        if row_loaded_date is not UNSET:
            field_dict["Row_Loaded_Date"] = row_loaded_date
        if site_summary_json is not UNSET:
            field_dict["Site_Summary_JSON"] = site_summary_json
        if sponsor_protocol_id is not UNSET:
            field_dict["Sponsor_Protocol_ID"] = sponsor_protocol_id
        if status_modified_date is not UNSET:
            field_dict["Status_Modified_Date"] = status_modified_date
        if study_metadata_json is not UNSET:
            field_dict["Study_Metadata_Json"] = study_metadata_json
        if ec_last_modified_date is not UNSET:
            field_dict["ec_last_modified_date"] = ec_last_modified_date
        if irb_protocol_id is not UNSET:
            field_dict["irb_protocol_id"] = irb_protocol_id
        if nct_number is not UNSET:
            field_dict["nct_number"] = nct_number
        if public_modified_data is not UNSET:
            field_dict["public_modified_data"] = public_modified_data
        if record_modified_date is not UNSET:
            field_dict["record_modified_date"] = record_modified_date
        if sitecore_start_date is not UNSET:
            field_dict["sitecore_start_date"] = sitecore_start_date
        if study_number is not UNSET:
            field_dict["study_number"] = study_number
        if unpub_start_date is not UNSET:
            field_dict["unpub_start_date"] = unpub_start_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.study_resource_site_summary_json_type_0_item import StudyResourceSiteSummaryJSONType0Item
        from ..models.study_resource_study_metadata_json_type_0 import StudyResourceStudyMetadataJsonType0

        d = dict(src_dict)
        pk_study = d.pop("pk_study")

        def _parse_contact_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contact_modified_date_type_0 = isoparse(data)

                return contact_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        contact_modified_date = _parse_contact_modified_date(d.pop("Contact_Modified_Date", UNSET))

        def _parse_current_study_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        current_study_status = _parse_current_study_status(d.pop("Current_Study_Status", UNSET))

        def _parse_eligibility_criteria(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        eligibility_criteria = _parse_eligibility_criteria(d.pop("Eligibility_Criteria", UNSET))

        def _parse_latest_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                latest_modified_date_type_0 = isoparse(data)

                return latest_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        latest_modified_date = _parse_latest_modified_date(d.pop("Latest_Modified_Date", UNSET))

        def _parse_metadata_added_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_added_date_type_0 = isoparse(data)

                return metadata_added_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        metadata_added_date = _parse_metadata_added_date(d.pop("Metadata_Added_Date", UNSET))

        def _parse_metadata_last_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                metadata_last_modified_date_type_0 = isoparse(data)

                return metadata_last_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        metadata_last_modified_date = _parse_metadata_last_modified_date(d.pop("Metadata_Last_Modified_Date", UNSET))

        def _parse_pi_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pi_modified_date_type_0 = isoparse(data)

                return pi_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        pi_modified_date = _parse_pi_modified_date(d.pop("PI_Modified_Date", UNSET))

        def _parse_poc_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        poc_id = _parse_poc_id(d.pop("POC_ID", UNSET))

        def _parse_publish_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        publish_state = _parse_publish_state(d.pop("Publish_State", UNSET))

        def _parse_row_loaded_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                row_loaded_date_type_0 = isoparse(data)

                return row_loaded_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        row_loaded_date = _parse_row_loaded_date(d.pop("Row_Loaded_Date", UNSET))

        def _parse_site_summary_json(data: object) -> Union[None, Unset, list["StudyResourceSiteSummaryJSONType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                site_summary_json_type_0 = []
                _site_summary_json_type_0 = data
                for site_summary_json_type_0_item_data in _site_summary_json_type_0:
                    site_summary_json_type_0_item = StudyResourceSiteSummaryJSONType0Item.from_dict(
                        site_summary_json_type_0_item_data
                    )

                    site_summary_json_type_0.append(site_summary_json_type_0_item)

                return site_summary_json_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["StudyResourceSiteSummaryJSONType0Item"]], data)

        site_summary_json = _parse_site_summary_json(d.pop("Site_Summary_JSON", UNSET))

        def _parse_sponsor_protocol_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sponsor_protocol_id = _parse_sponsor_protocol_id(d.pop("Sponsor_Protocol_ID", UNSET))

        def _parse_status_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_modified_date_type_0 = isoparse(data)

                return status_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        status_modified_date = _parse_status_modified_date(d.pop("Status_Modified_Date", UNSET))

        def _parse_study_metadata_json(data: object) -> Union["StudyResourceStudyMetadataJsonType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                study_metadata_json_type_0 = StudyResourceStudyMetadataJsonType0.from_dict(data)

                return study_metadata_json_type_0
            except:  # noqa: E722
                pass
            return cast(Union["StudyResourceStudyMetadataJsonType0", None, Unset], data)

        study_metadata_json = _parse_study_metadata_json(d.pop("Study_Metadata_Json", UNSET))

        def _parse_ec_last_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ec_last_modified_date_type_0 = isoparse(data)

                return ec_last_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        ec_last_modified_date = _parse_ec_last_modified_date(d.pop("ec_last_modified_date", UNSET))

        def _parse_irb_protocol_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        irb_protocol_id = _parse_irb_protocol_id(d.pop("irb_protocol_id", UNSET))

        def _parse_nct_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        nct_number = _parse_nct_number(d.pop("nct_number", UNSET))

        def _parse_public_modified_data(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                public_modified_data_type_0 = isoparse(data)

                return public_modified_data_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        public_modified_data = _parse_public_modified_data(d.pop("public_modified_data", UNSET))

        def _parse_record_modified_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                record_modified_date_type_0 = isoparse(data)

                return record_modified_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        record_modified_date = _parse_record_modified_date(d.pop("record_modified_date", UNSET))

        def _parse_sitecore_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sitecore_start_date_type_0 = isoparse(data)

                return sitecore_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        sitecore_start_date = _parse_sitecore_start_date(d.pop("sitecore_start_date", UNSET))

        def _parse_study_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        study_number = _parse_study_number(d.pop("study_number", UNSET))

        def _parse_unpub_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                unpub_start_date_type_0 = isoparse(data)

                return unpub_start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        unpub_start_date = _parse_unpub_start_date(d.pop("unpub_start_date", UNSET))

        study_resource = cls(
            pk_study=pk_study,
            contact_modified_date=contact_modified_date,
            current_study_status=current_study_status,
            eligibility_criteria=eligibility_criteria,
            latest_modified_date=latest_modified_date,
            metadata_added_date=metadata_added_date,
            metadata_last_modified_date=metadata_last_modified_date,
            pi_modified_date=pi_modified_date,
            poc_id=poc_id,
            publish_state=publish_state,
            row_loaded_date=row_loaded_date,
            site_summary_json=site_summary_json,
            sponsor_protocol_id=sponsor_protocol_id,
            status_modified_date=status_modified_date,
            study_metadata_json=study_metadata_json,
            ec_last_modified_date=ec_last_modified_date,
            irb_protocol_id=irb_protocol_id,
            nct_number=nct_number,
            public_modified_data=public_modified_data,
            record_modified_date=record_modified_date,
            sitecore_start_date=sitecore_start_date,
            study_number=study_number,
            unpub_start_date=unpub_start_date,
        )

        study_resource.additional_properties = d
        return study_resource

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
