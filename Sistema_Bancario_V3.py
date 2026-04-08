from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nasc, endereco):
        self.nome = nome
        self._cpf = cpf
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.contas = []

    @property
    def cpf(self):
        return self._cpf

    @staticmethod
    def validar_cpf(cpf):
        return len(cpf) == 11 and cpf.isdigit()

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Conta:
    def __init__(self, agencia, numero, usuario):
        self.agencia = agencia
        self._numero = numero
        self._usuario = usuario
        self._saldo = 0
        self._historico = Historico()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar()("Deposito", valor)
            print("Deposito realizado com sucesso")
        else:
            print("Valor insuficiente")

    def sacar(self,valor):
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3

        if valor > self.saldo:
            print("Saldo insuficiente")

        elif valor > self.limite:
            print("Valor acima do limite")

        elif self.numero_saques >= self.limite_saques:
            print("Limite de saque atingido")

        elif valor> 0:
            self.saldo -= valor
            self.numero_saques += 1
            self.historico.adicionar("Saque", valor)
            print("Saque realizado com sucesso")

        else:
            print("Valor inválido")

    def exibir_extrato(self):
        print("\n=========== EXTRATO ===========")

        if not self.historico.transacoes:
            print("Nenhuma movimentação")
        else:
            for t in self.historico.transacoes:
                print(t)
        print(f"\nSaldo: R$ {self.saldo: .2f}")
        print("===============================")

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def usuario(self):
        return self._usuario

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, usuario, numero):
        return cls("0001", numero, usuario)


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar(self, tipo,valor):
        self._transacoes.append(f'{tipo}: R$ {valor: 2f} - {datetime.now().strftime("%d-%m-%Y %H:%M")}')

    @property
    def transacoes(self):
        return self._transacoes


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def criar_usuario(usuarios):
    cpf = input("Digite o CPF: ")

    if filtrar_usuario(cpf, usuarios):
        print("Usuario já existe")
        return

    nome = input("Nome: ")
    data = input("Nascimento: ")
    endereco = input("Endereço: ")

    usuario = Usuario(nome, cpf, data, endereco)
    usuarios.append(usuario)

    print("Usuario criado")

def criar_conta(usuarios, contas, agencia):
    cpf = input("Digite o CPF: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuario não encontrado")
        return
    numero = len(contas) + 1
    conta = Conta.nova_conta(usuario, numero)

    usuario.adicionar_conta(conta)
    contas.append(conta)
    print("Conta criada")


def listar_contas(contas):
    for conta in contas:
        print("=" * 30)
        print(f'''
Agencia: {conta.agencia}
Conta: {conta.numero}
Titular: {conta.usuario.nome}
''')


def selecionar_conta(contas):
    numero = int(input("Número da conta: "))
    for conta in contas:
        if conta.numero == numero:
            return conta
    print("Conta não encontrada")
    return None

def menu():
    return int(input("""
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar usuário
[5] Criar conta
[6] Listar contas
[0] Sair
=> """))

usuarios = []
contas = []
AGENCIA = "0001"

while True:
    opcao = menu()

    if opcao == 1:
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Valor: "))
            conta.depositar(valor)

    elif opcao == 2:
        conta = selecionar_conta(contas)
        if conta:
            valor = float(input("Valor: "))
            conta.sacar(valor)

    elif opcao == 3:
        conta = selecionar_conta(contas)
        if conta:
            conta.exibir_extrato()

    elif opcao == 4:
        criar_usuario(usuarios)

    elif opcao == 5:
        criar_conta(usuarios, contas, AGENCIA)

    elif opcao == 6:
        listar_contas(contas)

    elif opcao == 0:
        print("Saindo do programa")
        break;

    else:
        print("Opção invalida!")
