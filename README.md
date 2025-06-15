# API_MirageGroup_6_Semestre_LLM

Repositório da API com RAG desenvolvida no 6º semestre do curso de Análise e Desenvolvimento de Sistemas – Fatec São José dos Campos.

---

##  Sumário

- [Sobre](#sobre)  
- [Tecnologias](#tecnologias)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação](#instalação)  
- [Endpoints](#endpoints)  
- [Estrutura do projeto](#estrutura-do-projeto)  

---

## Sobre

Esta API foi desenvolvida com o objetivo de integrar e expor modelos de Large Language Models (LLMs) via a plataforma **Groq**, utilizando a técnica de **RAG (Retrieval-Augmented Generation)** para enriquecer as respostas geradas com dados contextuais recuperados dinamicamente, para no fim criar um assistente que ajude pessoas que cuidam de pacientes com Alzheimer.

Funcionalidades principais:

- Conexão com LLMs de alto desempenho via **Groq API**;
- Suporte a múltiplas estratégias de modelo (ex: **Qwen**, **DeepSeek**);
- Enriquecimento de prompts com dados de uma base vetorial (RAG);
- Endpoint `/predict` que recebe entrada textual e retorna uma resposta gerada pelo modelo com enriquecimento semântico;
- Flexível para expansão com novas estratégias de modelo e prompt.

Este projeto foi desenvolvido como trabalho acadêmico no 6º semestre do curso de Análise e Desenvolvimento de Sistemas da FATEC São José dos Campos.

---

## Tecnologias

- **Python 3.11**  
- **LangChain**
- **FastAPI**  
- **ChromaDB**
- **MongoDB**
- **Uvicorn**  
- **Groq**  
- **dotenv**  

---

## Pré-requisitos

- Python 3.8 ou superior  
- Git  
- Groq API Key

---

## Instalação

```bash
git clone https://github.com/MirageGroup/API_MirageGroup_6_Semestre_LLM.git
cd API_MirageGroup_6_Semestre_LLM

# Crie e ative um ambiente virtual
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

```

## Endpoints

### `POST /predict`

Realiza a geração de resposta a partir de um modelo LLM, com enriquecimento de contexto via RAG.

**Body (JSON):**

```json
{
  "llm_model": "model1",  // "model1" = Qwen (padrão), "model2" = DeepSeek
  "text": "Quais os principais sintomas do Alzheimer?"
}
```

##  Estrutura do Projeto

```bash
.
├── main.py                    # Arquivo principal que define e executa a rota /predict
├── requirements.txt           # Lista de dependências Python
├── .env.sample                # Exemplo de variáveis de ambiente
├── .gitignore                 # Arquivos/pastas ignoradas pelo Git
├── README.md                  # Documentação do projeto

├── src/
│   ├── config.py              # Configurações do ambiente (dotenv)
│   ├── store.py               # Armazena configurações e variáveis de uso geral

│   ├── api/
│   │   ├── __init__.py
│   │   └── server.py          # Definições relacionadas ao servidor e roteamento

│   ├── models/
│   │   ├── __init__.py
│   │   ├── Model.py           # Classe principal que orquestra modelo e estratégia de prompt
│   │
│   │   ├── strategies/
│   │   │   ├── model/
│   │   │   │   ├── base.py               # Classe base para estratégias de modelo
│   │   │   │   ├── deepseek_strategy.py  # Implementação do modelo DeepSeek
│   │   │   │   └── qwen_strategy.py      # Implementação do modelo Qwen
│   │   │   └── systemMessage/
│   │   │       └── PadraoStrategy.py     # Estratégia padrão para mensagem do sistema

│   │   ├── retriever/
│   │   │   └── retriever.py    # Implementação do componente de recuperação (RAG)

│   │   └── vector_db/          # Pasta reservada para integração com banco vetorial
```