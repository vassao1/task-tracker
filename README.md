# task-tracker | pt-br
Task tracker simples em CLI feito para estudar postgres

Para utilizar, clone o repositório, abre aquele venv maroto e dá um ```pip install requirements.txt"```, após isso,  crie um arquivo ```.env``` e siga o exemplo do arquivo ```ENVEXAMPLE.txt``` de como preencher os campos necessários no .env para o funcionamento do código.

# Utilização:
Digite ```python3 cli.py --help``` para ver os comandos disponíveis.
```python3 cli.py listtasks``` irá mostrar todas as tarefas do banco de dados.
```python3 cli.py addtask "(tarefa)" (status)``` irá criar uma nova tarefa. Opções de status: 0 - Pendente, 1 - Em andamento, 2 - Concluída.
```python3 cli.py listbyid (id)``` lista a tarefa do ID inserido caso ela exista no banco de dados.
```python3 cli.py deletebyid (id)``` Deleta a tarefa de ID inserido do banco de dados.
```python3 cli.py deletall``` Deleta TODAS as tarefas do banco de dados.
```python3 cli.py updatetask (id) --task "(texto a ser inserido)" --status (status)``` Atualiza a task de ID inserido, os comandos `--task` e `--status` são opcionais (a pesar de que se nenhum dos dois for utilizado, nada irá acontecer), status segue a mesma lógica do `addtask`, 0 - Pendente, 1 - Em andamento, 2 - Concluída.
```python3 cli.py listbystatus (status)``` Lista todas as tarefas com o status inserido, segue a mesma lógica de números.
```python3 cli.py deletebystatus (status)``` Deleta todas as tarefas com o status inseredio, segue a mesma lógica de números.

IDs e datas são inseridos automaticamente pelo programa, data é atualizada ao atualizar a tarefa.

# task-tracker | eng
Simple CLI task tracker made to study PostgreSQL.

To use it, create a virtual environment, run ```pip install requirements.txt``` and then create a `.env` file and follow the example in the `ENVEXAMPLE.txt` file to fill in the necessary fields for the code to work.

# Usage:
Type ```python3 cli.py --help``` to see the available commands.  
```python3 cli.py listtasks``` will display all tasks in the database.  
```python3 cli.py addtask "(task)" (status)``` will create a new task. Status options: 0 - Pending, 1 - In Progress, 2 - Completed.  
```python3 cli.py listbyid (id)``` lists the task with the entered ID if it exists in the database.  
```python3 cli.py deletebyid (id)``` deletes the task with the entered ID from the database.  
```python3 cli.py deletall``` deletes ALL tasks from the database.  
```python3 cli.py updatetask (id) --task "(text to be inserted)" --status (status)``` updates the task with the entered ID. The `--task` and `--status` commands are optional (although if neither is used, nothing will happen). Status follows the same logic as `addtask`: 0 - Pending, 1 - In Progress, 2 - Completed.  
```python3 cli.py listbystatus (status)``` lists all tasks with the entered status, following the same number logic.  
```python3 cli.py deletebystatus (status)``` deletes all tasks with the entered status, following the same number logic.  

IDs and dates are automatically inserted by the program. The date is updated when the task is updated.
Although there's no english version of the program (all the CLI is in portuguese) i'll document in english too :p