from llm_chatbot import Model

chat1 = Model()
chat2 = Model('deepseek-r1-distill-llama-70b')

response = chat2.chat('Principais sintomas do Alzheimer')
for chunk in response:
    print(chunk, end="", flush=True)