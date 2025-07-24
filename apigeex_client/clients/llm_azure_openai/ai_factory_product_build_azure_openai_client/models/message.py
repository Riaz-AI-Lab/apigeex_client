from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_role import MessageRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_context_type_0 import MessageContextType0


T = TypeVar("T", bound="Message")


@_attrs_define
class Message:
    """A chat message.

    Attributes:
        role (MessageRole): The role of the author of this message.
        content (str): The contents of the message
        index (Union[Unset, int]): The index of the message in the conversation.
        recipient (Union[Unset, str]): The recipient of the message in the format of <namespace>.<operation>. Present if
            and only if the recipient is tool. Example: Contoso.productsUsingGET.
        end_turn (Union[Unset, bool]): Whether the message ends the turn.
        context (Union['MessageContextType0', None, Unset]): The conversation context
    """

    role: MessageRole
    content: str
    index: Union[Unset, int] = UNSET
    recipient: Union[Unset, str] = UNSET
    end_turn: Union[Unset, bool] = UNSET
    context: Union["MessageContextType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_context_type_0 import MessageContextType0

        role = self.role.value

        content = self.content

        index = self.index

        recipient = self.recipient

        end_turn = self.end_turn

        context: Union[None, Unset, dict[str, Any]]
        if isinstance(self.context, Unset):
            context = UNSET
        elif isinstance(self.context, MessageContextType0):
            context = self.context.to_dict()
        else:
            context = self.context

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )
        if index is not UNSET:
            field_dict["index"] = index
        if recipient is not UNSET:
            field_dict["recipient"] = recipient
        if end_turn is not UNSET:
            field_dict["end_turn"] = end_turn
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_context_type_0 import MessageContextType0

        d = dict(src_dict)
        role = MessageRole(d.pop("role"))

        content = d.pop("content")

        index = d.pop("index", UNSET)

        recipient = d.pop("recipient", UNSET)

        end_turn = d.pop("end_turn", UNSET)

        def _parse_context(data: object) -> Union["MessageContextType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                context_type_0 = MessageContextType0.from_dict(data)

                return context_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MessageContextType0", None, Unset], data)

        context = _parse_context(d.pop("context", UNSET))

        message = cls(
            role=role,
            content=content,
            index=index,
            recipient=recipient,
            end_turn=end_turn,
            context=context,
        )

        message.additional_properties = d
        return message

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
