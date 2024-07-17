import tkinter as tk
from tkinter import messagebox
import browser_cookie3

def clear_cookies(browser_name):
    try:
        if browser_name == "Chrome":
            cj = browser_cookie3.chrome()
        elif browser_name == "Firefox":
            cj = browser_cookie3.firefox()
        elif browser_name == "Edge":
            cj = browser_cookie3.edge()
        elif browser_name == "Opera":
            cj = browser_cookie3.opera()
        elif browser_name == "Brave":
            cj = browser_cookie3.brave()
        else:
            messagebox.showerror("Erro", "Navegador não suportado!")
            return

        count = 0
        for cookie in cj:
            cj.clear(cookie.domain, cookie.path, cookie.name)
            count += 1

        messagebox.showinfo("Sucesso", f"Cookies do {browser_name} excluídos com sucesso! Total: {count}")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao excluir cookies do {browser_name}: {e}")

def on_button_click():
    selected_browser = browser_var.get()
    if selected_browser:
        clear_cookies(selected_browser)
    else:
        messagebox.showwarning("Aviso", "Por favor, selecione um navegador.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Limpador de Cookies")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Selecione o navegador para limpar os cookies:", font=("Arial", 14))
label.pack(pady=10)

browser_var = tk.StringVar()

browsers = ["Chrome", "Firefox", "Edge", "Opera", "Brave"]
for browser in browsers:
    tk.Radiobutton(frame, text=browser, variable=browser_var, value=browser, font=("Arial", 12)).pack(anchor=tk.W)

button = tk.Button(root, text="Limpar Cookies", command=on_button_click, font=("Arial", 14))
button.pack(pady=20)

root.mainloop()
