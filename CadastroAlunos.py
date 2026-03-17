import sqlite3

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
        nome = input("Nome do aluno a ser cadastrado: ")
        ra = input("Digite seu RA: ")
        cursor.execute("INSERT INTO cadastro_alunos (nome, ra) VALUES (?,?)",
                       (nome, ra)
                       )

        conexao.commit()

    elif opcao == '2':
        cursor.execute("SELECT * FROM cadastro_alunos")

        alunos = cursor.fetchall()

        for aluno in alunos:
            print(aluno)

    elif opcao == '3':
        nome = (input("Digite o nome da pessoa que deseja remover da tabela: "))
        cursor.execute("DELETE FROM cadastro_alunos WHERE nome = ?", (nome,))
        conexao.commit()

    elif opcao == '4':
        break
