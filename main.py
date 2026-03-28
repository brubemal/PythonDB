import sqlite3
import func

conexao = sqlite3.connect("ListaAlunos.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cadastro_alunos(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               ra INTEGER NOT NULL UNIQUE
               )""")


while True:
    print("\n[1]Cadastrar Aluno")
    print("[2]Listar Alunos")
    print("[3]Remover Aluno")
    print("[4]Cancelar")

    opcao = input("\nEscolha uma das opcoes: ")

    if opcao == '1':
        func.cadastrar_aluno(cursor, conexao)

    elif opcao == '2':
        alunos = func.listar_alunos(cursor)

        for aluno in alunos:
            print(aluno)

    elif opcao == '3':
        func.deletar_aluno(cursor, conexao)

    elif opcao == '4':
        break
