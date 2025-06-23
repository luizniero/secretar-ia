# chat_server.py
import asyncio
import websockets
#from agent import run_agent
#from tools import check_availability, book_appointment

async def handle_connection(websocket):
    await websocket.send("Aguarde enquanto sou conectado ao sistema de agendamento...")
    async for message in websocket:
        print(f"[Usuário]: {message}")
        await websocket.send(f"Você disse: {message} — Em breve um atendente virtual irá te ajudar.")

#async def handle_agentic_connection(websocket):
#    #await websocket.send("Olá! Sou um assistente. Como posso te ajudar?")
#    async for message in websocket:
#        print(f"[Usuário]: {message}")
#        response = run_agent(message)
#        await websocket.send(response)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("Servidor WebSocket rodando em ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
