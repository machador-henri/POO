nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))

    nomes.append(nome)
    notas1.append(nota1)
    notas2.append(nota2)
    print("Estudante cadastrado. ")

def calcular_media(indice):
    return (notas1[indice] + notas2[indice]) / 2

def situacao(indice):
    media = calcular_media(indice)

    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"

    return "Reprovado"

def listar():
    if len(nomes) == 0: #len() retorna o tamanho da lista/
        print("Nenhum estudante cadastrado.")
        return

    print(f"\n{'NOME':<20}{'N1:':<5}{'N2:':<5}{'MEDIA':<8}{'SITUAÇÂO': <14}")

    for i in range (len(nomes)):
        print(f"{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}"f"{calcular_media(i):<8.1f}{situacao(i):<14}")

def menu():
    while True:
        print("\n1 - Cadastrar estudante")
        print("2 - Listar estudantes")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. ")

menu()