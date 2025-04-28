import typer # type: ignore
from db import *
from rich.table import Table # type: ignore
from rich.console import Console # type: ignore

app = typer.Typer()
console = Console()

@app.command()
def listtasks():
    if fetch_all() == None:
        print("Nenhuma tarefa encontrada.")
    else:
        table = Table("ID", "Tarefa", "Status", "Data da última atualização")
        for task in fetch_all():
            table.add_row(str(task[0]), task[1], task[2], task[3])
        console.print(table)

@app.command()
def addtask(task: str, status: int):
    if insert_task(task, status) == None:
        print("Erro ao adicionar tarefa.")
    else:
        print("Tarefa adicionada com sucesso.")

@app.command()
def listbyid(id: int):
    if fetch_specific(id) == None:
        print("Tarefa não encontrada, verifique o ID.")
    else:
        table = Table("ID", "Tarefa", "Status", "Data da última atualização")
        task = fetch_specific(id)
        table.add_row(str(task[0]), task[1], task[2], task[3])
        console.print(table)

@app.command()
def deletebyid(id: int):
    if delete_task(id) == None:
        print("Erro ao deletar tarefa, verifique o ID.")
    else:
        typer.confirm("Você tem certeza que deseja deletar essa tarefa?", abort=True)
        print("Tarefa deletada com sucesso.")    

@app.command()
def deleteall():
    if delete_all() == None:
        print("Erro ao deletar todas as tarefas.")
    else:
        typer.confirm("Você tem certeza que deseja deletar todas as tarefas?", abort=True)
        print("Todas as tarefas deletadas com sucesso.")

@app.command()
def updatetask(id: int, task: str = None, status: int = None):
    if fetch_specific(id) == None:
        print("Tarefa não encontrada, verifique o ID.")
    else:
        if task == None and status == None:
            print("Você deve informar o que deseja atualizar. Utilize o --help para mais informações.")
        else:
            update_task(id, task, status)
            print("Tarefa atualizada com sucesso.")

@app.command()
def listbystatus(status: int):
    if fetch_status(status) == None:
        print("Nenhuma tarefa encontrada com esse status.")
    else:
        table = Table("ID", "Tarefa", "Status", "Data da última atualização")
        for task in fetch_status(status):
            table.add_row(str(task[0]), task[1], task[2], task[3])
        console.print(table)

@app.command()
def deletebystatus(status: int):
    if fetch_status(status) == None:
        print("Não há nenhuma tarefa com esse status.")
    else:
        typer.confirm("Você tem certeza que deseja deletar todas as tarefas com esse status?", abort=True)
        delete_status(status)
        print("Todas as tarefas com esse status foram deletadas com sucesso.")

app()