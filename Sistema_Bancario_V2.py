# Sistema Bancário


saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

usuarios = []
contas = []


# MENU
def menu():
    return input("""

========= MENU =========

[1] Sacar
[2] Depositar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas

[0] Sair

=> """)


# DEPÓSITO (positional only)
def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: +R$ {valor:.2f}")
        print("Depósito realizado com sucesso.")

    else:
        print("Valor inválido.")

    return saldo, extrato


# SAQUE (keyword only)
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print("Saldo insuficiente.")

    elif valor > limite:
        print("Valor acima do limite permitido.")

    elif numero_saques >= limite_saques:
        print("Limite de saques diários atingido.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: -R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso.")

    else:
        print("Valor inválido.")

    return saldo, extrato


# EXTRATO (positional + keyword)
def exibir_extrato(saldo, /, *, extrato):

    print("\n========== EXTRATO ==========")

    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao in extrato:
            print(operacao)

    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================\n")


# FILTRAR USUÁRIO
def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf
    ]

    return usuarios_filtrados[0] if usuarios_filtrados else None


# CRIAR USUÁRIO
def criar_usuario(usuarios):

    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, numero, bairro, cidade/sigla): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso.")


# CRIAR CONTA
def criar_conta(agencia, numero_conta, usuarios):

    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso.")
        return {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }

    print("Usuário não encontrado.")


# LISTAR CONTAS
def listar_contas(contas):

    for conta in contas:
        linha = f"""
Agência:\t{conta['agencia']}
Conta:\t\t{conta['numero_conta']}
Titular:\t{conta['usuario']['nome']}
"""
        print("=" * 30)
        print(linha)


# LOOP PRINCIPAL
while True:

    opcao = menu()

    if opcao == "1":

        valor = float(input("Informe o valor do saque: "))

        saldo, extrato = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "2":

        valor = float(input("Informe o valor do depósito: "))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "3":

        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":

        criar_usuario(usuarios)

    elif opcao == "5":

        numero_conta = len(contas) + 1

        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "6":

        listar_contas(contas)

    elif opcao == "0":

        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")