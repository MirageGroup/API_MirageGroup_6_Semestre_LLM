from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

class Model:
    def __init__(self, model_name='qwen-2.5-32b', temperature=0.7):
        self.system_message = SystemMessage(content=(
            "Você é um assistente cuja função é responder dúvidas sobre a doença Alzheimer "
            "e tirar dúvidas que uma pessoa cuidadora/responsável por alguém com essa doença possa vir a ter. "
            "Mantenha suas respostas nesse escopo e caso seja feita uma pergunta fora dele, "
            "educadamente explique que não pode responder."
        ))

        api_key=os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("A chave da api não foi encontrada.")
        
        self.model = ChatGroq(model_name=model_name, temperature=temperature, api_key=api_key)
        self.history = ChatMessageHistory()
        self.history.add_message(self.system_message)

    def chat(self, prompt: str) -> str:
        self.history.add_message(HumanMessage(content=prompt))

        response = self.model.invoke(self.history.messages)

        self.history.aadd_messages(AIMessage(content=response.content))


        return response.content