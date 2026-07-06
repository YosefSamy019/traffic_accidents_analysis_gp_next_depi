from abc import ABC, abstractmethod


class AgentTool(ABC):
    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_parameters(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def execute(self, parameters: dict) -> dict:
        raise NotImplementedError
