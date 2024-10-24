import tkinter as tk
from tkinter import messagebox
from database import adicionar_tarefa, listar_tarefas, remover_tarefa, editar_tarefa

class GerenciadorTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Tarefas")

        # Label e Entry para título
        self.label_titulo = tk.Label(root, text="Título da Tarefa")
        self.label_titulo.pack()
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        # Label e Entry para descrição
        self.label_descricao = tk.Label(root, text="Descrição")
        self.label_descricao.pack()
        self.entry_descricao = tk.Entry(root)
        self.entry_descricao.pack()

        # Label e Entry para prioridade
        self.label_prioridade = tk.Label(root, text="Prioridade")
        self.label_prioridade.pack()
        self.entry_prioridade = tk.Entry(root)
        self.entry_prioridade.pack()

        # Botão para adicionar tarefa
        self.botao_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.botao_adicionar.pack()

        # Lista de tarefas
        self.lista_tarefas = tk.Listbox(root)
        self.lista_tarefas.pack()

        # Botão para remover tarefa
        self.botao_remover = tk.Button(root, text="Remover Tarefa", command=self.remover_tarefa)
        self.botao_remover.pack()

        self.carregar_tarefas()

    def carregar_tarefas(self):
        tarefas = listar_tarefas()
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in tarefas:
            self.lista_tarefas.insert(tk.END, f"{tarefa[0]} - {tarefa[1]} (Prioridade: {tarefa[3]})")

    def adicionar_tarefa(self):
        titulo = self.entry_titulo.get()
        descricao = self.entry_descricao.get()
        prioridade = self.entry_prioridade.get()

        if titulo == "" or prioridade == "":
            messagebox.showwarning("Erro", "Título e prioridade são obrigatórios")
        else:
            adicionar_tarefa(titulo, descricao, int(prioridade))
            self.carregar_tarefas()

    def remover_tarefa(self):
        try:
            tarefa_selecionada = self.lista_tarefas.get(self.lista_tarefas.curselection())
            tarefa_id = tarefa_selecionada.split(" - ")[0]
            remover_tarefa(tarefa_id)
            self.carregar_tarefas()
        except:
            messagebox.showwarning("Erro", "Selecione uma tarefa para remover")


if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTarefas(root)
    root.mainloop()
