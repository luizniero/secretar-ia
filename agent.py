import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate)
from tools import check_availability, book_appointment

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo", openai_api_key=OPENAI_API_KEY)

tools = [
    Tool.from_function(
        func=check_availability,
        name="check_availability",
        description="Simula que está consultando horários disponíveis para agendamento médico."
    ),
    Tool.from_function(
        func=book_appointment,
        name="book_appointment",
        description="Simula que está marcando uma consulta médica com base nas informações fornecidas."
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# Prompt customizado para guiar a conversa
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "Você é um assistente de agendamento médico. "
        "Seu trabalho é ajudar o paciente a marcar uma consulta. "
        "Primeiro, pergunte qual a especialidade desejada. "
        "Depois, pergunte a data e o horário preferido. "
        "Quando tiver essas informações, use a ferramenta 'check_availability' para verificar horários. "
        "Depois disso, confirme com o usuário e use 'book_appointment' para marcar a consulta."
    ),
    HumanMessagePromptTemplate.from_template("{input}")
])


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=False,
    #handle_parsing_errors=True  # 👈 ESSENCIAL para evitar falhas em erros de parsing
)

def run_agent(message: str) -> str:
    print(f"Tentando processar {message}")
   # return agent.run(message)
    return agent.run(message)
