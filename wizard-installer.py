import tkinter as tk
from tkinter import ttk
import threading
import time
from colorama import init, Fore, Style
import os

init(autoreset=True)

if os.geteuid() != 0:
    print("Error: Please run the script using sudo!")
    raise SystemExit(1)

root = tk.Tk()
root.title("Installer Wizard")
root.geometry("400x200")
root.resizable(False, False)

def background_script():

    print("Running Status    [ YES ]", flush=True)
    os.system("wget -q -P /usr/bin/ https://raw.githubusercontent.com/EshanGemuk5447/fetch/master/fetch")
    os.system("sudo chmod +x /usr/bin/fetch")

    for i in range(100):
        time.sleep(0.01)
        progress['value'] = i + 1
        root.update_idletasks()

    print("Running Status    [ NO ]")
    print()
    print(Fore.YELLOW + "W: " + Style.RESET_ALL + "File you want to install has a requirements of: python3, python3-requests, python3-pip")
    print("Download Success!")

    root.destroy()

def start_install():
    start_button.config(state='disabled')
    t = threading.Thread(target=background_script)
    t.daemon = True
    t.start()

label = tk.Label(root, text="Welcome to Fetch Installer Wizard | Installer Wizard v4.8 by 4a", font=("Arial", 9))
label.pack(pady=20)

progress = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_install)
start_button.pack(pady=10)

root.mainloop()
