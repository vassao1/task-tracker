import psycopg2 as pg
from dotenv import load_dotenv
import os
import arrow # type: ignore

load_dotenv()

def parsed_now():
    return arrow.now().format('HH:mm, DD/MM/YY')

def status_translate(status: int):
    if status == 0:
        return "Pendente"
    elif status == 2:
        return "Concluída"
    elif status == 1:
        return "Em andamento"
    else:
        return None

def create_connection():
    conn = pg.connect(database=os.getenv("database"),
                    host=os.getenv("host"),
                    user=os.getenv("user"),
                    password=os.getenv("password"),
                    port=os.getenv("port"))
    return conn

def create_table():
    conn = create_connection()
    if conn is None:
        return ("Falha ao conectar na DB.")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, task TEXT NOT NULL, status TEXT NOT NULL, date TEXT NOT NULL);")
    conn.commit()
    conn.close()

def fetch_all():
    conn = create_connection()
    if conn is None:
        return ("Falha ao conectar na DB.")
    cur = conn.cursor()
    create_table()
    
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        return None
    return rows

def fetch_specific(id: int):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return row

def insert_task(task: str, status: int):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    date = parsed_now()
    status = status_translate(status)

    cur = conn.cursor()
    cur.execute(f"INSERT INTO tasks (task, status, date) VALUES ('{task}', '{status}', '{date}');")
    conn.commit()
    conn.close()
    return True

def delete_task(id: int):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    if fetch_specific(id) == None:
        return ("Tarefa não encontrada, verifique o ID.")
    cur = conn.cursor()
    cur.execute(f"DELETE FROM tasks WHERE id = {id}")
    conn.commit()
    conn.close()
    return True

def delete_all():
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
    return True

def update_task(id, task=None, status=None):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    if fetch_specific(id) == None:
        return False
    
    infos = []
    
    if task is not None:
        infos.append(f"task = '{task}'")
    if status is not None:
        infos.append(f"status = '{status_translate(status)}'")
    if not infos:
        return False
    infos.append(f"date = '{parsed_now()}'")
    infos.append(f"id = {id}")

    cur = conn.cursor()
    cur.execute(f"UPDATE tasks SET {', '.join(infos[:-1])} WHERE {infos[-1]}")
    conn.commit()
    conn.close()
    return True

def fetch_status(status: int):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM tasks WHERE status = '{status_translate(status)}'")
    rows = cur.fetchall()
    conn.close()
    if not rows:
        return None
    return rows

def delete_status(status: int):
    conn = create_connection()
    if conn is None:
        return None
    create_table()
    
    if fetch_status(status) == None:
        return ("Nenhuma tarefa encontrada com esse status.")
    
    cur = conn.cursor()
    cur.execute(f"DELETE FROM tasks WHERE status = '{status_translate(status)}'")
    conn.commit()
    conn.close()
    return True

# To do: Fazer um fetch por data, mas pra isso tenho que melhorar o sistema de data ou pensar em um jeito diferente de fazer.