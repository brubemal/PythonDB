import sqlite3

conexao = sqlite3.connect("IMC.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS imc(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    peso INTEGER NOT NULL,
    altura INTEGER NOT NULL,
    nivelIMC TEXT NOT NULL
)
""")

nome = input("Digite seu nome: ")
altura = int(input("Digite sua altura em cm: "))  
peso = int(input("Digite seu peso em kg: "))      

altura_m = altura / 100

IMC = round(peso / (altura_m ** 2))

if IMC >= 18.5 and IMC <= 25:
    nivel = "Normal"
elif IMC < 18.5:
    nivel = "Magreza"
else:
    nivel = "Sobrepeso"

print(f"Seu IMC é {IMC} e você está no nível {nivel}")

cursor.execute("""
INSERT INTO imc (nome, peso, altura, nivelIMC)
VALUES (?, ?, ?, ?)
""", (nome, peso, altura, nivel))

conexao.commit()
conexao.close()

print("Dados salvos com sucesso!")