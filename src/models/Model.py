from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import HumanMessage, AIMessage
from src.retriever.retriever import augmented_prompt

from ..models.strategies.model.base import ModelStrategy
from ..models.strategies.systemMessage.base import SystemMessageStrategy

class Model:
    def __init__(self, model_strategy: ModelStrategy, system_message_strategy: SystemMessageStrategy):
        self.model_strategy = model_strategy
        self.model = model_strategy.get_model()
        self.history = ChatMessageHistory()

        self.system_message = system_message_strategy.get_message()
        self.history.add_message(self.system_message)

    def chat(self, prompt: str):
        self.history.add_message(HumanMessage(content=augmented_prompt(prompt)))
        return self._stream_response()

    def _stream_response(self):
        response_content = ''
        capturando = False  # Flag para controlar quando começar a exibir ao usuário

        for chunk in self.model.stream(self.history.messages):
            if chunk.content:
                response_content += chunk.content

                if not capturando:
                    if '</think>' in chunk.content.lower():
                        capturando = True
                        depois_think = chunk.content.lower().split('</think>', 1)[-1]
                        if depois_think.strip():
                            yield depois_think
                else:
                    yield chunk.content

        # No histórico: salva TODO o conteúdo (incluindo o <think>)
        self.history.add_messages(AIMessage(content=response_content))
