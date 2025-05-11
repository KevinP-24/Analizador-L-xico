import sys
import os
import tkinter as tk
from tkinter import ttk
from lexer import Lexer
from errores import ErrorLexico

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

        # Instancia del analizador léxico
        self.lexer = Lexer()

    def analizar(self):
        codigo = self.entrada_codigo.get("1.0", tk.END)

        try:
            tokens = self.lexer.analizar(codigo)
            self.salida.config(state='normal')
            self.salida.delete("1.0", tk.END)

            for token in tokens:
                lexema = token['lexema']
                categoria = token['categoria']
                linea = token['linea']
                columna = token['columna']
                self.salida.insert(tk.END, f"{categoria:25} | {lexema:<15} (línea {linea}, columna {columna})\n")

            self.salida.config(state='disabled')

        except ErrorLexico as e:
            self.salida.config(state='normal')
            self.salida.delete("1.0", tk.END)
            self.salida.insert(tk.END, str(e))
            self.salida.config(state='disabled')

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = AnalizadorGUI(root)
    root.mainloop()
