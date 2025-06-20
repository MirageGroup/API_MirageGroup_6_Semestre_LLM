from abc import ABC, abstractmethod
from langchain_core.messages import BaseMessage
from typing import List, Iterator


class ModelStrategy(ABC):
    @abstractmethod
    def get_model(self) -> str:

        pass
