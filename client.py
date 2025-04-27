import socket
import pyautogui
import os
import time

server_ip = os.environ.get('SERVER_IP')
if not server_ip:
    server_ip = input("Enter server IP: ")  # fallback for debugging

PORT = 5000

def connect_to_server(ip, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            client_socket.connect((ip, port))
            print(f"Connected to server at {ip}:{port}")
            return client_socket
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 3 seconds...")
            time.sleep(3)

# Try to connect
client = connect_to_server(server_ip, PORT)

# Once connected, start receiving commands
while True:
    data = client.recv(1024).decode()
    if not data:
        break  # Connection lost
    if data.startswith("MOVE"):
        _, x, y = data.split()
        pyautogui.moveTo(int(x), int(y))
    elif data.startswith("CLICK"):
        _, x, y, button, pressed = data.split()
        pyautogui.click(int(x), int(y))
