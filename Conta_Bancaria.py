#Conta bancaria

saldo = 0
depositos = []  # lista para depósitos
saques = []     # lista para saques
cont_saques = 0  # contador de saques diários

def menu():
    while True:
        opcao = input("""
Bem vindo ao Banco DIO, o que gostaria de fazer?

[1] - Sacar
[2] - Depositar
[3] - Extrato
[0] - Sair

""")
        if opcao == "1":
            sacar()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            ver_extrato()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

def sacar():
    global saldo, cont_saques
    if cont_saques >= 3:
        print("Limite de 3 saques diários atingido.")
        return
    while True:
        try:
            saque = float(input("Informe qual valor gostaria de sacar (máx. 500): "))
            if saque > 500:
                print("Valor inválido, máximo 500.")
            elif saque <= 0:
                print("Valor deve ser positivo.")
            elif saque > saldo:
                print(f"Saldo insuficiente. Saldo atual: R$ {saldo:.2f}")
            else:
                saldo -= saque
                cont_saques += 1
                saques.append(saque)  # adiciona à lista de saques
                print(f"Saque realizado. Saldo atual: R$ {saldo:.2f}")
                break
        except ValueError:
            print("Entrada inválida. Digite um número.")

def depositar():
    global saldo
    while True:
        try:
            depositar_valor = float(input("Informe qual valor gostaria de depositar: "))
            if depositar_valor > 0:
                saldo += depositar_valor
                depositos.append(depositar_valor)  # adiciona à lista de depósitos
                print(f"Depósito realizado. Saldo atual: R$ {saldo:.2f}")
                break
            else:
                print("Valor deve ser positivo.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def ver_extrato():
    print("\nExtrato:")
    if not depositos and not saques:
        print("Nenhuma transação realizada.")
    else:
        if depositos:
            print("Depósitos:")
            for d in depositos:
                print(f"  +R$ {d:.2f}")
        if saques:
            print("Saques:")
            for s in saques:
                print(f"  -R$ {s:.2f}")

    # Contar usando o tamanho das listas
    num_depositos = len(depositos)
    num_saques = len(saques)
    print(f"\nTotal de depósitos realizados: {num_depositos}")
    print(f"Total de saques realizados: {num_saques}")
    print(f"Saldo atual: R$ {saldo:.2f}\n")

menu()