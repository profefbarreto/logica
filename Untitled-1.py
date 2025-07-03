import tkinter as tk
from tkinter import messagebox

def submit():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    altura = float(entry_altura.get())
    
    messagebox.showinfo("Cadastro", f"{nome} cadastrado com sucesso!\nCom {idade} anos e {altura}m.")
    
    if idade >= 18:
        messagebox.showinfo("Idade", "Maior de idade!")
    else:
        messagebox.showinfo("Idade", "Menor de idade!")

# Create the main window
root = tk.Tk()
root.title("Academia Vip X")

# Create and place the widgets
label_welcome = tk.Label(root, text="Bem-vindo a academia Vip X")
label_welcome.pack()

label_separator = tk.Label(root, text="==========================")
label_separator.pack()

label_nome = tk.Label(root, text="Digite o nome do cliente:")
label_nome.pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

label_idade = tk.Label(root, text="Digite a idade do cliente:")
label_idade.pack()
entry_idade = tk.Entry(root)
entry_idade.pack()

label_altura = tk.Label(root, text="Digite a altura do cliente:")
label_altura.pack()
entry_altura = tk.Entry(root)
entry_altura.pack()

button_submit = tk.Button(root, text="Submit", command=submit)
button_submit.pack()

# Run the application
root.mainloop()
