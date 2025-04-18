
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import HumanMessage, AIMessage

class Model:
    def __init__(self, model_strategy, system_message_strategy):
        self.model = model_strategy.get_model()
        self.history = ChatMessageHistory()

        self.system_message = system_message_strategy.get_message()
        self.history.add_message(self.system_message)

    def chat(self, prompt: str):
        self.history.add_message(HumanMessage(content=prompt))
        return self._stream_response()

    def _stream_response(self):
        response_content = ''
        for chunk in self.model.stream(self.history.messages):
            if chunk.content:
                response_content += chunk.content
                yield chunk.content

        self.history.add_messages(AIMessage(content=response_content))