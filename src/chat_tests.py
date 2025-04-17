from models.llm_chatbot import Model

chat1 = Model()
chat2 = Model('deepseek-r1-distill-llama-70b')

response = chat1.chat('Ele tem quanto tempo de vida?')
for chunk in response:
    print(chunk, end="", flush=True)