import socket
import threading
from constants import PORT, SERVER_IP

lobbies = {1: [], 2: [], 3: []}
names = {}

def handle_client(client, lobby_id, player_name):
    try:
        lobbies[lobby_id].append(client)
        names[client] = player_name
        broadcast(f"Server: {player_name} has joined the lobby.", lobby_id, client)
        ready_status = {client: False}

        while True:
            msg = client.recv(1024).decode('utf-8')
            if msg == 'EXIT':
                break
            elif msg.startswith("READY"):
                ready = msg.split(",")[1] == "True"
                ready_status[client] = ready
                count_ready = sum(ready_status[c] for c in ready_status)
                broadcast(f"Server: {count_ready}/2 Ready", lobby_id)
            else:
                broadcast(f"{player_name}: {msg}", lobby_id, client)
    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        if client in lobbies[lobby_id]:
            lobbies[lobby_id].remove(client)
        broadcast(f"Server: {player_name} has left the lobby.", lobby_id)
        if client in names:
            del names[client]
        client.close()

def broadcast(msg, lobby_id, sender=None):
    for client in lobbies[lobby_id]:
        if client != sender:
            client.send(msg.encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen()
    print(f"Server started on {SERVER_IP}:{PORT}")

    while True:
        client, addr = server.accept()
        print(f"New connection from {addr}")

        data = client.recv(1024).decode('utf-8')
        try:
            lobby_id, player_name = data.split(",")
            lobby_id = int(lobby_id)
            if lobby_id in lobbies:
                thread = threading.Thread(target=handle_client, args=(client, lobby_id, player_name))
                thread.start()
        except ValueError:
            print("Invalid data received from client:", data)

if __name__ == "__main__":
    start_server()
