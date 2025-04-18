from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from models.strategies.systemMessage.PadrãoStrategy import PadrãoMessageStrategy

from ..models.llm_chatbot import Model
from ..models.strategies.model.qwen_strategy import QwenModelStrategy
from ..models.strategies.model.deepseek_strategy import DeepseekModelStrategy

app = FastAPI()

class InputData(BaseModel):
    llm_model: str = ''
    text: str

@app.post("/predict")
def predict(data: InputData):
    if not data.text:
        return {"message": "texto não informado", "input": data.text}

    prompt_strategy = PadrãoMessageStrategy()

    if data.llm_model in ('model1', ''):
        model_strategy = QwenModelStrategy()
    elif data.llm_model == 'model2':
        model_strategy = DeepseekModelStrategy()
    else:
        return {"message": "Modelo não reconhecido", "input": data.text}

    chatbot = Model(model_strategy, prompt_strategy)
    response = chatbot.chat(data.text)
    return StreamingResponse(response)
