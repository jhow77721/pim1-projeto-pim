import json
import statistics

alunos = []

def carregar_dados():
    global alunos
    try:
        with open("alunos.json", "r") as arquivo:
            alunos = json.load(arquivo)
    except FileNotFoundError:
        alunos = []

def salvar_dados():
    with open("alunos.json", "w") as arquivo:
        json.dump(alunos, arquivo, indent=4)

def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    idade = input("Idade: ")
    nota = input("Nota (0 a 10): ")

    aluno = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(aluno)
    salvar_dados()
    print("Aluno cadastrado com sucesso!")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']}")

def estatisticas():
    if not alunos:
        print("Nenhum dado disponível.")
        return
    notas = [float(a['nota']) for a in alunos]
    print(f"Média das notas: {statistics.mean(notas):.2f}")
    print(f"Moda das notas: {statistics.mode(notas)}")
    print(f"Mediana das notas: {statistics.median(notas)}")

def limpar_dados():
    global alunos
    alunos = []
    salvar_dados()
    print("Todos os dados foram apagados com sucesso!")

def menu():
    carregar_dados()
    while True:
        print("\n--- MENU ---")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Estatísticas")
        print("4 - Sair")
        print("5 - Limpar todos os dados")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            estatisticas()
        elif opcao == "4":
            print("Saindo...")
            break
        elif opcao == "5":
            limpar_dados()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()