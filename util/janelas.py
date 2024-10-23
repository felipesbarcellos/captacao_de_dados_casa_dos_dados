import tkinter as tk
from tkinter import filedialog
from util.constants import OUTPUT_PATH

class SiteCarregado():
    def __init__(self):
        self.root = tk.Tk()
        self.frame = self.construir_janela()
        self.frame.pack(padx=10, pady=10)
        self.root.mainloop()

    def construir_janela(self):
        frame = tk.Frame(self.root)
        tk.Label(frame, text="O navegador foi carregado com sucesso.\nAgora, preencha os filtros").pack()
        tk.Button(frame, text="OK", command=self.root.destroy).pack()
        return frame

class FiltrosSelecionados():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-topmost', True)
        self.root.geometry("600x150+0-0")
        self.root.config(background="lightgrey")
        self.frame = self.construir_janela()
        self.frame.config(border=10)
        self.frame.pack(padx=10, pady=10)
        self.root.mainloop()

    def construir_janela(self):
        frame = tk.Frame(self.root)
        label = tk.Label(frame, text="Se você já selecionou todos os filtros, selecione agora nome e caminho de saída do arquivo CSV:")
        label.pack()
        caminho_frame = tk.Frame(frame)
        caminho_frame.pack(pady=7.5)
        self.caminho_entry = tk.Entry(caminho_frame, width=50)
        self.caminho_entry.pack(side="left")

        self.botao_selecionar = tk.Button(caminho_frame, text="Escolher local de saida", command=self.selecionar_arquivo_saida)
        self.botao_selecionar.pack()
        button_ok = tk.Button(frame, text="OK", command=self.ok_pressed, width=20, bg="lightblue", fg="black")
        button_ok.pack()
        return frame
    
    def ok_pressed(self):
        output_file = self.caminho_entry.get()
        try:
            with open(OUTPUT_PATH, mode="x"):
                pass
        except FileExistsError:
            with open(OUTPUT_PATH, mode="w", encoding="utf-8") as f:
                f.write(output_file)

    def selecionar_arquivo_saida(self):
        """Abre um diálogo para o usuário selecionar um arquivo e atualiza o rótulo."""
        arquivo = filedialog.asksaveasfilename(defaultextension=".csv",
                                          filetypes=[("Todos os arquivos", "*.*"),
                                                    ("Arquivos CSV", "*.csv")])
        self.caminho_entry.delete(0, tk.END)
        self.caminho_entry.insert(0, arquivo)

if __name__ == "__main__":
    # FiltrosSelecionados()
    SiteCarregado()