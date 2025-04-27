import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

def start_server():
    if getattr(sys, 'frozen', False):
        executable = os.path.join(sys._MEIPASS, 'server.py')
    else:
        executable = 'server.py'
    
    subprocess.Popen([sys.executable, executable])
    root.destroy()

def start_client():
    ip = ip_entry.get()
    if not ip:
        messagebox.showerror("Error", "Please enter the Server IP Address!")
        return
    
    os.environ['SERVER_IP'] = ip

    if getattr(sys, 'frozen', False):
        executable = os.path.join(sys._MEIPASS, 'client.py')
    else:
        executable = 'client.py'
    
    subprocess.Popen([sys.executable, executable])
    root.destroy()

# --- GUI Setup ---
root = tk.Tk()
root.title("Mouse & Keyboard Share")
root.geometry("400x350")
root.resizable(False, False)

# Load and set window icon
try:
    from PIL import Image, ImageTk
    icon_path = os.path.join(os.path.dirname(__file__), 'assets', 'share-link.png')
    icon_img = Image.open(icon_path)
    icon_photo = ImageTk.PhotoImage(icon_img)
    root.iconphoto(False, icon_photo)
except Exception as e:
    print(f"Could not load icon: {e}")

# Optional: Show image inside the app
try:
    logo_label = tk.Label(root, image=icon_photo)
    logo_label.pack(pady=10)
except Exception as e:
    print(f"Could not display logo: {e}")

title_label = tk.Label(root, text="Mouse & Keyboard Share", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

server_btn = tk.Button(btn_frame, text="Start as Server", width=20, height=2, command=start_server)
server_btn.grid(row=0, column=0, padx=10)

client_btn = tk.Button(btn_frame, text="Start as Client", width=20, height=2, command=start_client)
client_btn.grid(row=0, column=1, padx=10)

ip_label = tk.Label(root, text="Server IP (for Client only):", font=("Arial", 12))
ip_label.pack(pady=5)

ip_entry = tk.Entry(root, width=30)
ip_entry.pack()

root.mainloop()
