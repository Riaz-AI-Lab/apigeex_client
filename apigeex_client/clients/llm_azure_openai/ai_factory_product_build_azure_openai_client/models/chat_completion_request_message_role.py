from enum import Enum


class ChatCompletionRequestMessageRole(str, Enum):
    ASSISTANT = "assistant"
    FUNCTION = "function"
    SYSTEM = "system"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
