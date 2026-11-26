from mysql.connector import Error
import funcionarios as func
from utils import mostrar

def menu_funcionarios():
    while True:
        print("\n--- FUNCIONARIOS ---")
        print("1-Cadastrar  2-Listar  3-Atualizar  4-Excluir  0-Voltar")
        op = input("Opcao: ").strip()
        try:
            if op == "1":
                func.criar(input("Nome: "), input("CPF: "),
                           input("Cargo: "), input("E-mail: "))
                print("Funcionario cadastrado!")
            elif op == "2":
                mostrar(func.listar())
            elif op == "3":
                alterados = func.atualizar(int(input("ID: ")), input("Novo nome: "),
                                           input("Novo cargo: "), input("Novo e-mail: "))
                print("Atualizado!" if alterados else "Nada alterado (ID nao existe?).")
            elif op == "4":
                apagados = func.excluir(int(input("ID: ")))
                print("Excluido!" if apagados else "ID nao encontrado.")
            elif op == "0":
                break
            else:
                print("Opcao invalida.")
        except ValueError as erro:
            print(f"Dado invalido: {erro}")
        except Error as erro:
            print(f"Erro no banco de dados: {erro}")