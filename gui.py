import sys
import os

# Añadir la carpeta 'automatas' al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'automatas'))

from afd import AFD
from lexer import analizar
import tkinter as tk
from tkinter import ttk
from lexer import analizar
from afd import AFD

class AnalizadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - Scala")
        self.root.geometry("800x600")

        # Entrada de código
        self.label = ttk.Label(root, text="Ingrese código Scala:")
        self.label.pack(pady=5)

        self.entrada_codigo = tk.Text(root, height=10)
        self.entrada_codigo.pack(fill=tk.BOTH, expand=True, padx=10)

        # Botón analizar
        self.boton = ttk.Button(root, text="Analizar", command=self.analizar)
        self.boton.pack(pady=10)

        # Resultados
        self.label_resultado = ttk.Label(root, text="Tokens reconocidos:")
        self.label_resultado.pack()

        self.salida = tk.Text(root, height=15, state='disabled')
        self.salida.pack(fill=tk.BOTH, expand=True, padx=10)

        # AFD para identificadores
        self.afd = AFD()

    def analizar(self):
        codigo = self.entrada_codigo.get("1.0", tk.END)
        try:
            tokens = analizar(codigo)
            self.salida.config(state='normal')
            self.salida.delete("1.0", tk.END)

            for tipo, valor in tokens:
                val_afd = self.afd.validar(valor) if tipo == 'IDENTIFIER' else "-"
                self.salida.insert(tk.END, f"{tipo:15} | {valor:20} | AFD: {val_afd}\n")

            self.salida.config(state='disabled')
        except Exception as e:
            self.salida.config(state='normal')
            self.salida.delete("1.0", tk.END)
            self.salida.insert(tk.END, f"Error: {e}")
            self.salida.config(state='disabled')

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorGUI(root)
    root.mainloop()
