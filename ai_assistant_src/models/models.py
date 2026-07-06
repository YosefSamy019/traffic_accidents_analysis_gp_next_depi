from abc import ABC, abstractmethod
from enum import Enum


class AgentStatus(Enum):
    RUNNING = 'running'
    STOPPED = 'stopped'


class ChatMsg(ABC):
    def __init__(self):
        self.expired = False

    @abstractmethod
    def to_json(self) -> dict:
        raise NotImplementedError


class UserChatMsg(ChatMsg):

    def __init__(self, content: str):
        super().__init__()
        self.content = content

    def to_json(self) -> dict:
        return {"role": 'user', "content": self.content}


class AssistantChatMsg(ChatMsg):
    def __init__(self, content: str, reasoning: str, tool_calls: list, dump):
        super().__init__()

        self.content = content if content else ""
        self.reasoning = reasoning if reasoning else ''
        self.dump = dump

        # FIX: Use model_dump() to preserve ALL fields (including Gemini's hidden signatures)
        # instead of manually rebuilding the dictionary.
        self.tool_calls = [tc.model_dump() for tc in tool_calls] if tool_calls else []

    def to_json(self) -> dict:
        msg = {
            "role": "assistant",
            "content": self.content,
        }

        if self.tool_calls:
            msg["tool_calls"] = self.tool_calls

        return msg

class SystemChatMsg(ChatMsg):
    def __init__(self, content: str):
        super().__init__()

        self.content = content

    def to_json(self) -> dict:
        return {"role": 'system', "content": self.content}

class ToolCallChatMsg(ChatMsg):
    def __init__(
            self,
            tool_call_id,
            function_name,
            function_arguments,
            result,
            original_assistant_msg_dump=None, # Kept for signature compatibility if needed, but unused here
    ):
        super().__init__()

        self.function_name = function_name
        self.tool_call_id = tool_call_id
        self.function_arguments = function_arguments
        self.result = result

    def to_json(self):
        # Standard OpenAI Tool Message format.
        # The proxy handles matching this to the intact Assistant tool call.
        return {
            "role": "tool",
            "content": self.result,
            "tool_call_id": self.tool_call_id,
        }