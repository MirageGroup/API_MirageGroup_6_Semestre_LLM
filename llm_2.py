from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)
from langchain_groq import ChatGroq
import os 
from dotenv import load_dotenv

history = ChatMessageHistory()
load_dotenv()

groq_api_key = os.environ["GROQ_API_KEY"]

chat = ChatGroq(temperature=0.7, model_name='deepseek-r1-distill-llama-70b', api_key=groq_api_key)

history.add_message(SystemMessage(content='Você é um assistente cuja função é responder dúvidas sobre a doença Alzheimer e tirar dúvidas que uma pessoa cuidadora/responsável por alguém com essa doença possa vir a ter. Mantenha suas respostas nesse escopo e caso seja feita uma pergunta fora dele, educadamente explique que não pode responder.'))

def chat_qwen_history(input):
    history.add_message(HumanMessage(content=input))
    
    response = chat.invoke(history.messages)
    
    history.add_message(AIMessage(content=response.content))
    
    return response.content

print(chat_qwen_history("Me explique bancos não relacionais."))
