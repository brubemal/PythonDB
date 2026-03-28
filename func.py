import sqlite3


def cadastrar_aluno(cursor, conexao):
    nome = input("Nome do aluno a ser cadastrado: ")
    ra = input("Digite seu RA: ")
    try:
        cursor.execute("INSERT INTO cadastro_alunos (nome, ra) VALUES (?,?)", (nome, ra))
        conexao.commit()
        print("Aluno cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print("Erro: RA já cadastrado. Use um RA diferente.")
    except Exception as e:
        print(f"Erro ao cadastrar aluno: {e}")


def listar_alunos(cursor):
    cursor.execute("SELECT * FROM cadastro_alunos")
    return cursor.fetchall()


def deletar_aluno(cursor, conexao):
    nome = input("Digite o nome da pessoa que deseja remover da tabela: ")
    try:
        cursor.execute("DELETE FROM cadastro_alunos WHERE nome = ?", (nome,))
        conexao.commit()
        print("Aluno removido com sucesso.")
    except Exception as e:
        print(f"Erro ao remover aluno: {e}")
