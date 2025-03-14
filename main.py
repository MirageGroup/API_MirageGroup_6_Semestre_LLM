# from connection import Models

# chatbot = Models()

# resposta1 = chatbot.chat_1("O que é Alzheimer?")
# print("Resposta do modelo 1:", resposta1)


# resposta2 = chatbot.chat_1("Quais são os sintomas do Alzheimer?")
# print("Resposta do modelo 2:", resposta2)


from llm_chatbot import Model

chatbot_qwen = Model()
chatbot_deepseek = Model('deepseek-r1-distill-llama-70b')

resposta1 = chatbot_qwen.chat("O que é Alzheimer?")
print("Resposta do modelo 1:", resposta1)

resposta2 = chatbot_deepseek.chat("Quais os cinco principais sintomas do Alzheimer?")
print("Resposta do modelo 2:", resposta2)