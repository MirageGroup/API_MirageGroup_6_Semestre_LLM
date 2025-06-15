import src.config  # Carrega o .env logo no começo
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import time 

from ..models.strategies.systemMessage.PadraoStrategy import PadrãoMessageStrategy

from ..models.Model import Model
from ..models.strategies.model.qwen_strategy import QwenModelStrategy
from ..models.strategies.model.deepseek_strategy import DeepseekModelStrategy

app = FastAPI()

class InputData(BaseModel):
    llm_model: str = ''
    text: str

@app.post("/predict")
def predict(data: InputData):
    import time
    from fastapi.responses import JSONResponse

    if not data.text:
        return {"message": "texto não informado", "input": data.text}

    start = time.time()

    prompt_strategy = PadrãoMessageStrategy()

    if data.llm_model in ('model1', ''):
        model_strategy = QwenModelStrategy()
    elif data.llm_model == 'model2':
        model_strategy = DeepseekModelStrategy()
    else:
        return {"message": "Modelo não reconhecido", "input": data.text}

    chatbot = Model(model_strategy, prompt_strategy)
    response = chatbot.chat(data.text)  # supondo que retorne uma string ou objeto serializável

    end = time.time()
    tempo_execucao = end - start
    

    # Retorna JSON com o conteúdo da resposta + tempo
    return {
        "response": response,
        "tempo_execucao": tempo_execucao
    }
