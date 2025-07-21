from enum import Enum


class InnerErrorCode(str, Enum):
    RESPONSIBLEAIPOLICYVIOLATION = "ResponsibleAIPolicyViolation"

    def __str__(self) -> str:
        return str(self.value)
