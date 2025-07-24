from enum import Enum


class ContentFilterResultSeverity(str, Enum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    SAFE = "safe"

    def __str__(self) -> str:
        return str(self.value)
