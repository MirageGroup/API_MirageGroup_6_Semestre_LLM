from abc import ABC, abstractmethod
from langchain_core.messages import SystemMessage


class SystemMessageStrategy(ABC):
    @abstractmethod
    def get_system_message(self) -> SystemMessage:
        pass