# from connection import Models

# chatbot = Models()

# resposta1 = chatbot.chat_1("O que é Alzheimer?")
# print("Resposta do modelo 1:", resposta1)


# resposta2 = chatbot.chat_1("Quais são os sintomas do Alzheimer?")
# print("Resposta do modelo 2:", resposta2)



from llm_chatbot import Model
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.response import StreamingResponse

app = FastAPI()

class InputData(BaseModel):
    llm_model:str
    text: str

@app.post("/predict")
def predict(data: InputData):
    chatbot_qwen = Model()
    chatbot_deepseek = Model('deepseek-r1-distill-llama-70b')

    
    if data.text == '':
        return {"message": "texto não informado", "input": data.text}
    

    if data.llm_model == 'model1' or data.llm_model == '':
        response = chatbot_qwen.chat(data.text)
        return StreamingResponse(response)
    elif data.llm_model == 'model2':
        response = chatbot_deepseek.chat(data.text)
        return StreamingResponse(response)
    else:
        return {"message": "Modelo não reconhecido", "input": data.text}
    

# Para rodar o servidor: uvicorn main:app --reload
