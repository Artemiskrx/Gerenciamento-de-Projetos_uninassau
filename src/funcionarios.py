from db import executar
from validacoes import validar_texto, validar_cpf, validar_email

   # CREATE
def criar(nome, cpf, cargo, email):                   
    nome = validar_texto(nome, "Nome")
    cpf = validar_cpf(cpf)
    cargo = validar_texto(cargo, "Cargo")
    email = validar_email(email)
    sql = "INSERT INTO funcionarios (nome, cpf, cargo, email) VALUES (%s, %s, %s, %s)"
    return executar(sql, (nome, cpf, cargo, email))

  # READ (todos)

def listar():                                          
    return executar("SELECT * FROM funcionarios ORDER BY id", consulta=True)

# READ (um)

def buscar(id_func):                                     
    linhas = executar("SELECT * FROM funcionarios WHERE id = %s",
                      (id_func,), consulta=True)
    return linhas[0] if linhas else None

    # UPDATE

def atualizar(id_func, nome, cargo, email):          
    nome = validar_texto(nome, "Nome")
    cargo = validar_texto(cargo, "Cargo")
    email = validar_email(email)
    sql = "UPDATE funcionarios SET nome = %s, cargo = %s, email = %s WHERE id = %s"
    return executar(sql, (nome, cargo, email, id_func))

    # DELETE

def excluir(id_func):                                    # DELETE
    return executar("DELETE FROM funcionarios WHERE id = %s", (id_func,))