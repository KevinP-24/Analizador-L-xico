import tkinter as tk
from tkinter import ttk
from lexer import Lexer
from errores import ErrorLexico

class AnalizadorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Analizador Léxico - Scala")
        self.root.geometry("940x680")
        self.root.configure(bg="#f7f7f7")
        self.root.resizable(False, False)

        # ===== Estilos Modernos =====
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6, background="#ffffff")
        style.map("TButton",
                  background=[("active", "#d0d0d0")],
                  relief=[("pressed", "sunken")])

        style.configure("Hover.TButton", background="#d0d0d0")

        style.configure("TLabel", background="#f7f7f7", font=("Segoe UI", 11, "bold"))

        # ===== Etiqueta entrada =====
        ttk.Label(root, text="Ingrese código Scala:").pack(pady=(15, 5))

        entrada_frame = tk.Frame(root, bg="#f7f7f7", bd=1, relief="groove")
        entrada_frame.pack(fill=tk.BOTH, expand=False, padx=20)

        self.entrada_codigo = tk.Text(
            entrada_frame, height=10, font=("Consolas", 11), bg="#ffffff", relief="flat", padx=8, pady=8
        )
        self.entrada_codigo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_entrada = ttk.Scrollbar(entrada_frame, command=self.entrada_codigo.yview)
        scroll_entrada.pack(side=tk.RIGHT, fill=tk.Y)
        self.entrada_codigo.config(yscrollcommand=scroll_entrada.set)

        # ===== Botón analizar =====
        self.boton = ttk.Button(root, text="🧠 Analizar Código", command=self.analizar)
        self.boton.pack(pady=15)
        self.boton.bind("<Enter>", lambda e: self.boton.config(style="Hover.TButton"))
        self.boton.bind("<Leave>", lambda e: self.boton.config(style="TButton"))

        # ===== Separador =====
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=20, pady=10)

        # ===== Etiqueta salida =====
        ttk.Label(root, text="Tokens reconocidos:").pack()

        resultado_frame = tk.Frame(root, bg="#f7f7f7", bd=1, relief="groove")
        resultado_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(5, 20))

        self.salida = tk.Text(
            resultado_frame,
            height=15,
            font=("Consolas", 11),
            bg="#f4f4f4",
            relief="flat",
            padx=8,
            pady=8,
            state='disabled'
        )
        self.salida.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scroll_salida = ttk.Scrollbar(resultado_frame, command=self.salida.yview)
        scroll_salida.pack(side=tk.RIGHT, fill=tk.Y)
        self.salida.config(yscrollcommand=scroll_salida.set)

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

            self.salida.insert(tk.END, f"\n→ Total de tokens: {len(tokens)}\n")
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
