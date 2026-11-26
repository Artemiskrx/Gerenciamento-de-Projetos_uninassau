# Gerenciamento-de-Projetos_uninassau
## Gerenciador de Projetos

## Pariticpantes:
Carlos Roberto -> Banco de dados
Antonio Vitor -> git/github, pastas do repositorio
Thyago -> Modulo do menu
David -> Modulo funcionários


## Modelo de dados


<img width="437" height="211" alt="docs" src="https://github.com/user-attachments/assets/dfd1b92f-c9ad-4731-86ef-e5a45a2feba4" />

funcionarios: id (PK), nome, cpf (único), cargo, email (único)
projetos: id (PK), nome, prazo, orcamento, descricao, funcionario_id (FK → funcionarios.id)
Tecnologias usadas
Python 3.10+: lógica do sistema, validações e menu no terminal
MySQL 8: banco de dados com duas tabelas relacionadas (1:N)
mysql-connector-python: biblioteca que conecta o Python ao MySQL
Git e GitHub: controle de versão e trabalho em equipe
Estrutura do projeto
```
gerenciamento-projetos/
├── sql/
│   ├── schema.sql           # criação do banco e das tabelas
│   ├── sql_dados.sql        # dados de teste
│   └── consultas.sql        # consultas úteis (JOIN, SUM)
├── src/
│   ├── db.py                # conexão e função executar
│   ├── validacoes.py        # CPF, e-mail, orçamento e prazo
│   ├── utils.py             # formatação da saída
│   ├── funcionarios.py      # CRUD de funcionários
│   ├── projetos.py          # CRUD de projetos
│   ├── menu_funcionarios.py
│   ├── menu_projetos.py
│   └── main.py              # menu principal
├── sql/docs.png             # diagrama do banco
├── requirements.txt
└── README.md
```
Como executar
1. Pré-requisitos
Python 3.10 ou mais novo, MySQL Server 8, MySQL Workbench e Git.
2. Criar e ativar o ambiente virtual (PowerShell, na pasta do projeto)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```
Se a ativação for bloqueada, execute `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` e tente novamente.
3. Instalar as dependências
```powershell
python -m pip install -r requirements.txt
```
4. Criar o banco de dados no MySQL Workbench
Inicie o servidor MySQL, abra `sql/schema.sql` no Workbench e execute o script. Opcionalmente, abra e execute `sql/sql_dados.sql` para carregar dados de teste.
5. Definir as variáveis de ambiente
A senha do banco não fica no código. No PowerShell, defina antes de executar e mantenha este terminal aberto:
```powershell
$env:DB_PASSWORD="sua_senha"
```
Variável	Padrão	Descrição
`DB_HOST`	`localhost`	Servidor do MySQL
`DB_USER`	`root`	Usuário do MySQL
`DB_NAME`	`gerenciamento_projetos`	Nome do banco
`DB_PASSWORD`	(vazio)	Senha do MySQL
6. Executar o sistema (na pasta raiz do projeto)
```powershell
python .\src\main.py
```

```$env:DB_PASSWORD = "sua_senha_do_mysql"
python .\src\main.py
```

No VS Code, selecione o interpretador `.venv` usando **Python: Select Interpreter**.
Validações
CPF: exige 11 dígitos, sem validar os dígitos verificadores (aceita com ou sem pontuação)
E-mail: formato válido
Orçamento: número maior que zero
Prazo: formato DD/MM/AAAA, data real e não pode estar no passado
Relacionamento: não é possível criar projeto para funcionário inexistente nem excluir
funcionário que ainda possui projetos
Problemas comuns
Access denied for user: senha em `DB_PASSWORD` errada, ou o terminal foi reaberto sem definir a variável.
Can't connect to MySQL server: o serviço do MySQL está desligado.
Unknown database: o `schema.sql` ainda não foi executado.
ModuleNotFoundError: ambiente virtual não ativado ou faltou `pip install -r requirements.txt`.
