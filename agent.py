# agent.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializar o LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7)

# Histórico de chat global
chat_history = []

# Definir o prompt do chat
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um assistente de chat prestativo e amigável. Responda às perguntas dos usuários de forma clara e concisa. "
            "Sua principal função é conversar e responder às dúvidas gerais."
        ),
        MessagesPlaceholder(variable_name="chat_history"), # Usamos 'chat_history' aqui
        ("human", "{input}"),
    ]
)

# Criar a cadeia de conversa diretamente
# Esta cadeia vai receber o 'input' (mensagem do usuário) e o 'chat_history'
chain = prompt | llm

def run_chat_agent(user_message: str) -> str:
    global chat_history # Indica que vamos modificar a variável global

    try:
        # Adiciona a mensagem do usuário ao histórico ANTES de invocar a cadeia
        chat_history.append(HumanMessage(content=user_message))

        # Invoca a cadeia com a mensagem atual e o histórico completo
        response = chain.invoke({"input": user_message, "chat_history": chat_history})
        
        # A resposta do LLM é do tipo AIMessage, adicione-a ao histórico
        chat_history.append(AIMessage(content=response.content))

        return response.content
    except Exception as e:
        print(f"Erro ao executar o chat: {e}")
        return "Desculpe, houve um erro ao processar sua solicitação."


def reset_chat_history():
    """Reseta o histórico do chat."""
    global chat_history # Indica que vamos modificar a variável global
    chat_history = []
    print("Histórico do chat foi resetado.")