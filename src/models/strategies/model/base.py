from abc import ABC, abstractmethod
from langchain_core.messages import BaseMessage
from typing import List, Iterator


class ModelStrategy(ABC):
    @abstractmethod
    def stream_response(self, messages: List[BaseMessage]) -> Iterator[str]:
        pass