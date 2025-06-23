# tools.py
from langchain.tools import tool
import datetime

class Ferramentas:
    @tool
    def consulta_disponibilidade(data: str, servico: str) -> str:
        """
        Verifica a disponibilidade de horários para um serviço em uma data específica na agenda do Google.
        Formato da data esperado: AAAA-MM-DD.
        Retorna uma string com os horários disponíveis ou uma mensagem de indisponibilidade.
        Por enquanto, apenas registra a chamada da função.
        """
        try:
            # Em um cenário real, você faria uma chamada à API do Google Calendar aqui.
            # No momento, estamos apenas registrando a intenção.
            requested_date = datetime.datetime.strptime(data, "%Y-%m-%d").date() # Apenas para validar o formato da data
            print(f"[LOG TOOL] Chamada: consulta_disponibilidade(data={data}, servico={servico})")
            return f"CONSULTA DE DISPONIBILIDADE: Verificando disponibilidade para '{servico}' em '{data}' na agenda do Google (apenas log)."
        except ValueError:
            return "Formato de data inválido. Por favor, use AAAA-MM-DD."
        except Exception as e:
            return f"Ocorreu um erro ao verificar a disponibilidade: {e}"

    @tool
    def agenda_consulta(data: str, horario: str, servico: str, nome_cliente: str) -> str:
        """
        Agenda um compromisso para um serviço em uma data e horário específicos na agenda do Google.
        Formato da data esperado: AAAA-MM-DD. Formato do horário esperado: HH:MM.
        Retorna uma string de confirmação ou erro.
        Por enquanto, apenas registra a chamada da função.
        """
        try:
            # Em um cenário real, você faria uma chamada à API do Google Calendar para inserir um evento.
            # No momento, estamos apenas registrando a intenção.
            appointment_datetime = datetime.datetime.strptime(f"{data} {horario}", "%Y-%m-%d %H:%M") # Apenas para validar os formatos
            print(f"[LOG TOOL] Chamada: agenda_consulta(data={data}, horario={horario}, servico={servico}, nome_cliente={nome_cliente})")
            return f"AGENDAMENTO DE CONSULTA: Agendando '{servico}' para '{nome_cliente}' em '{data}' às '{horario}' na agenda do Google (apenas log)."
        except ValueError:
            return "Formato de data ou hora inválido. Use AAAA-MM-DD para data e HH:MM para hora."
        except Exception as e:
            return f"Ocorreu um erro ao agendar: {e}"