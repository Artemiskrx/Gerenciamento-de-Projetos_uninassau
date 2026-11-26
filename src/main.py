from menu_funcionarios import menu_funcionarios
from menu_projetos import menu_projetos
def menu_principal():
    while True:
        print("\n=== GERENCIAMENTO DE PROJETOS ===")
        print("1-Funcionarios  2-Projetos  0-Sair")
        op = input("Opcao: ").strip()
        if op == "1":
            menu_funcionarios()
        elif op == "2":
            menu_projetos()
        elif op == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida.")
if __name__ == "__main__":
    menu_principal()