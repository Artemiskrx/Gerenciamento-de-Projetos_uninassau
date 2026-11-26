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
│   ├── dados_exemplo.sql    # dados de teste
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
├── docs/der.png
├── requirements.txt
└── README.md
```
Como executar
1. Pré-requisitos
Python 3.10 ou mais novo, MySQL Server e Git.
2. Baixar o projeto
```bash
git clone LINK_DO_REPOSITORIO
cd gerenciamento-projetos
```
3. Criar o ambiente virtual e instalar as dependências
```bash
python -m venv venv

# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```
4. Criar o banco de dados
```bash
mysql -u root -p < sql/schema.sql
```
Opcional: carregar dados de exemplo para testar.
```bash
mysql -u root -p gerenciamento_projetos < sql/dados_exemplo.sql
```
5. Definir as variáveis de ambiente
A senha do banco não fica no código. Defina antes de rodar
(troque `sua_senha` pela senha do seu MySQL):
```bash
# Windows (cmd):
set DB_PASSWORD=sua_senha
# Windows (PowerShell):
$env:DB_PASSWORD="sua_senha"
# Linux/macOS:
export DB_PASSWORD=sua_senha
```
Variável	Padrão	Descrição
`DB_HOST`	`localhost`	Servidor do MySQL
`DB_USER`	`root`	Usuário do MySQL
`DB_NAME`	`gerenciamento_projetos`	Nome do banco
`DB_PASSWORD`	(vazio)	Senha do MySQL
6. Executar o sistema
```bash
cd src
python main.py
```
Validações
CPF: 11 dígitos, dígitos verificadores corretos (aceita com ou sem pontuação)
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
