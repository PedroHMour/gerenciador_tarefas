import sqlite3

def conectar():
    conn = sqlite3.connect("tarefas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            prioridade INTEGER
        )
        """
    )
    conn.commit()
    return conn

def adicionar_tarefa(titulo, descricao, prioridade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (titulo, descricao, prioridade) VALUES (?, ?, ?)", (titulo, descricao, prioridade))
    conn.commit()
    conn.close()

def listar_tarefas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    return tarefas   

def remover_tarefa(tarefa_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id=?", (tarefa_id,))
    conn.commit()
    conn.close()

def editar_tarefa(tarefa_id, novo_titulo, nova_descricao, nova_prioridade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET titulo=?, descricao=?, prioridade=? WHERE id=?", (novo_titulo, nova_descricao, nova_prioridade, tarefa_id)) 
    conn.commit()
    conn.close()