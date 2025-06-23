# agent.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Inicializar o LLM
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.7) # Aumentei um pouco o temperature para respostas mais variadas

# Definir o prompt do chat
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Você é um assistente de chat prestativo e amigável. Responda às perguntas dos usuários de forma clara e concisa. "
            "Sua principal função é conversar e responder às dúvidas gerais."
        ),
        MessagesPlaceholder(variable_name="history"), # Usamos 'history' aqui para o RunnableWithMessageHistory
        ("human", "{input}"),
    ]
)

# Criar a cadeia de conversa
chain = prompt | llm

# Gerenciador de histórico de sessão (vamos usar uma sessão única por enquanto)
# Em um sistema real com múltiplos usuários, você passaria uma session_id diferente para cada um.
store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Criar o runnable com histórico de mensagens
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# ID de sessão padrão para nosso exemplo de um único chat
SESSION_ID = "chat_session_1"

def run_chat_agent(user_message: str) -> str:
    try:
        # Chamar a cadeia de conversa com histórico
        response = with_message_history.invoke(
            {"input": user_message},
            config={"configurable": {"session_id": SESSION_ID}}
        )
        return response.content
    except Exception as e:
        print(f"Erro ao executar o chat: {e}")
        return "Desculpe, houve um erro ao processar sua solicitação."

def reset_chat_history():
    """Reseta o histórico do chat para a sessão padrão."""
    if SESSION_ID in store:
        del store[SESSION_ID]
    print(f"Histórico do chat para a sessão '{SESSION_ID}' foi resetado.")