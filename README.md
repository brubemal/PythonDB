# PythonDB
Repositório criado com o objetivo de treinar meus estudos em Python e Banco de Dados, incluindo projetos pessoais desenvolvidos durante o aprendizado.

# PythonDB
Repositório criado com o objetivo de treinar meus estudos em Python e Banco de Dados, incluindo projetos pessoais desenvolvidos durante o aprendizado.

## Tecnologias Utilizadas

- **Python 3**
- **SQLite3** — banco de dados local
- **Módulo personalizado** `func.py` — separação das funções

---

## Estrutura do Projeto

projeto/
├── main.py       # Arquivo principal com o menu
├── func.py       # Funções de cadastro, listagem e remoção
└── ListaAlunos.db  # Banco de dados gerado automaticamente


---

## Banco de Dados

**Tabela:** `cadastro_alunos`

| Campo | Tipo    | Restrições                  |
|-------|---------|-----------------------------|
| id    | INTEGER | PRIMARY KEY, AUTOINCREMENT  |
| nome  | TEXT    | NOT NULL                    |
| ra    | INTEGER | NOT NULL, UNIQUE            |

---

## Funcionalidades

### [1] Cadastrar Aluno
Solicita nome e RA do aluno e insere no banco de dados. O RA deve ser único.

### [2] Listar Alunos
Exibe todos os alunos cadastrados no banco.

### [3] Remover Aluno
Remove um aluno pelo RA, garantindo que não haja remoção acidental de alunos homônimos.

### [4] Sair
Encerra o programa.

---

## Melhorias Aplicadas

### 1. Separação de Funções (`func.py`)
As funções foram movidas para um arquivo separado, deixando o `main.py` limpo e fácil de manter. As funções são importadas com:

### 2. Tratamento de Erros
Cada função possui seu próprio tratamento de erro, seguindo o princípio de responsabilidade individual:

### 3. Remoção por RA
A remoção passou a usar o RA como identificador único, evitando o risco de remover alunos com nomes iguais.





