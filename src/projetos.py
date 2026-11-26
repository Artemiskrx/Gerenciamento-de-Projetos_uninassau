from db import executar
from validacoes import validar_texto, validar_orcamento, validar_prazo

# CREATE

def criar(nome, prazo, orcamento, descricao, funcionario_id):   
    nome = validar_texto(nome, "Nome")
    prazo = validar_prazo(prazo)
    orcamento = validar_orcamento(orcamento)
    sql = ("INSERT INTO projetos (nome, prazo, orcamento, descricao, funcionario_id) "
           "VALUES (%s, %s, %s, %s, %s)")
    return executar(sql, (nome, prazo, orcamento, descricao.strip(), funcionario_id))

# READ (todos)

def listar():                                                   
    sql = ("SELECT p.id, p.nome, p.prazo, p.orcamento, f.nome AS responsavel "
           "FROM projetos p JOIN funcionarios f ON f.id = p.funcionario_id "
           "ORDER BY p.prazo")
    return executar(sql, consulta=True)

# READ (1:N)

def listar_por_funcionario(funcionario_id):                     
    sql = "SELECT * FROM projetos WHERE funcionario_id = %s ORDER BY prazo"
    return executar(sql, (funcionario_id,), consulta=True)

# UPDATE

def atualizar(id_proj, nome, prazo, orcamento, descricao):      
    nome = validar_texto(nome, "Nome")
    prazo = validar_prazo(prazo)
    orcamento = validar_orcamento(orcamento)
    sql = ("UPDATE projetos SET nome = %s, prazo = %s, orcamento = %s, "
           "descricao = %s WHERE id = %s")
    return executar(sql, (nome, prazo, orcamento, descricao.strip(), id_proj))

# DELETE 

def excluir(id_proj):                                              
    return executar("DELETE FROM projetos WHERE id = %s", (id_proj,))