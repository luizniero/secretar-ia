from langchain_core.tools import tool

@tool
def check_availability(data: str) -> str:
    """Consulta horários disponíveis para agendamento."""
    print(f"Camou o check_availabiity com a data: {data}")
    return "Horários disponíveis: Segunda às 14h, Terça às 16h, Sexta às 10h."

@tool
def book_appointment(info: str) -> str:
    """Marca uma consulta médica com base nas informações fornecidas."""
    print(f"Chamou o book_appointment com a info: {info}")
    return f"Consulta marcada com sucesso para {info}!"
