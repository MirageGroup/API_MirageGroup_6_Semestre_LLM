# strategies/chatgroq_strategy.py
from langchain_groq import ChatGroq
from .base import ModelStrategy
import os

class QwenModelStrategy(ModelStrategy):
    def __init__(self, model_name='qwen-qwq-32b', temperature=0.7):
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY não foi encontrada")

    def get_model(self):
        return ChatGroq(model_name=self.model_name, temperature=self.temperature, api_key=self.api_key)