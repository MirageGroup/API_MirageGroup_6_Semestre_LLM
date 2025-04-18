from abc import ABC, abstractmethod
from langchain_core.messages import SystemMessage


class SystemMessageStrategy(ABC):
    @abstractmethod
    def get_message(self) -> SystemMessage:
        pass