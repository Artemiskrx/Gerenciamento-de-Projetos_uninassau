from mysql.connector import Error
import projetos as proj
from utils import mostrar
def menu_projetos():
    while True:
        print("\n--- PROJETOS ---")
        print("1-Cadastrar  2-Listar  3-Listar por funcionario  "
              "4-Atualizar  5-Excluir  0-Voltar")
        op = input("Opcao: ").strip()
        try:
            if op == "1":
                proj.criar(input("Nome: "), input("Prazo (DD/MM/AAAA): "),
                           input("Orcamento: "), input("Descricao: "),
                           int(input("ID do funcionario responsavel: ")))
                print("Projeto cadastrado!")
            elif op == "2":
                mostrar(proj.listar())
            elif op == "3":
                mostrar(proj.listar_por_funcionario(int(input("ID do funcionario: "))))
            elif op == "4":
                alterados = proj.atualizar(int(input("ID: ")), input("Novo nome: "),
                                           input("Novo prazo (DD/MM/AAAA): "),
                                           input("Novo orcamento: "),
                                           input("Nova descricao: "))
                print("Atualizado!" if alterados else "Nada alterado (ID nao existe?).")
            elif op == "5":
                apagados = proj.excluir(int(input("ID: ")))
                print("Excluido!" if apagados else "ID nao encontrado.")
            elif op == "0":
                break
            else:
                print("Opcao invalida.")
        except ValueError as erro:
            print(f"Dado invalido: {erro}")
        except Error as erro:
            print(f"Erro no banco de dados: {erro}")   