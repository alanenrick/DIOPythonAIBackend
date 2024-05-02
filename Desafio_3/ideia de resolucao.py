import time
from decimal import Decimal
from abc import ABC, abstractmethod, abstractclassmethod

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, cliente, numero):
        self._saldo = Decimal("0.00")
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor > self.saldo:
            print("Operação falhou! Saldo insuficiente!")
            return False
        else:
            self._saldo -= valor
            return True

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False

class ContaCorrente(Conta):
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.limite = Decimal("500.00")
        self.LIMITE_SAQUES = 0
        self.quantidade_saques = 0

    def sacar(self, valor):
        limite_excedido = valor > self.limite
        saques_excedidos = self.quantidade_saques >= self.LIMITE_SAQUES

        if limite_excedido:
            print("Operação falhou! Limite excedido!")
            return False
        elif saques_excedidos:
            print("Operação falhou! Limite de saques excedidos!")
            return False
        else:
            super().sacar(valor)
            self.quantidade_saques += 1

    def __str__(self):
        return f"Agência: {self.agencia}, C/C: {self.numero}, Cliente: {self.cliente.nome}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": time.strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def depositar(conta, valor):
    if valor > 0:
        Deposito(valor).registrar(conta)
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(valor, conta):
    if valor > 0:
        Saque(valor).registrar(conta)
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")

def exibir_extrato(conta):
    historico = conta.historico.transacoes
    data_hora = time.localtime()
    data = time.strftime('%d/%m/%Y', data_hora)
    hora = time.strftime('%H:%M:%S', data_hora)

    extrato_formatado = "Não há registro de movimentações.\n" if not historico else historico

    saldo_formatado = f"\nSaldo em {data} {hora}: R$ {conta.saldo:.2f}"

    print("\n===================== EXTRATO =====================")
    print("\n===================================================")
    print("Data/Hora          |   Operação    |    Valor")
    print("===================================================")
    for transacao in extrato_formatado:
        print(f"{transacao['data']}  |  {transacao['tipo']}  |  {transacao['valor']}")
    print(saldo_formatado)
    print("======================= FIM =======================")

def verifica_saldo(conta):
    if conta.saldo > 0:
        return True
    else:
        return False

def menu_cliente():
    return input("""
    Seja bem-vindo(a)!

    [1] Entrar
    [2] Cadastrar Cliente
    [0] Sair

    Digite a opção desejada e pressione [Enter]: 
    """)

def menu_conta():
    return input("""
    [1] Acessar conta
    [2] Criar conta
    [3] Listar contas
    [0] Sair

    Digite a opção desejada e pressione [Enter]: 
    """)

def menu_transacoes():
    return input("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

    Digite a opção desejada e pressione [Enter]: 
    """)

def acesso_menu_transacoes(conta):
    while True:
        opcao = menu_transacoes()

        if opcao == "1":  # Depositar
            valor = Decimal(input("Informe o valor do depósito: R$ "))
            depositar(conta, valor)

        elif opcao == "2":  # Sacar
            com_saldo = verifica_saldo(conta)
            if not com_saldo:
                print("Saque não disponível. Verifique seu saldo.")
            else:
                valor = Decimal(input("Informe o valor do saque: R$ "))
                sacar(valor, conta)

        elif opcao == "3":  # Exibir extrato
            exibir_extrato(conta)

        elif opcao == "9":  # Voltar para o menu_conta
            print("Voltando ao menu de Contas")
            return acesso_menu_conta()

        elif opcao == "0":  # Fechar programa
            print("Obrigado por usar nossos Serviços!")
            break

        else:  # Opção inválida
            print("Operação inválida, por favor selecione uma opção disponível.")

def acesso_menu_conta(cliente):
    while True:
        opcao = menu_conta()

        if opcao == "1":  # Acessar menu transações da conta
            numero_conta = input("Digite o número da conta: ")
            conta_encontrada = None
            for conta in cliente.contas:
                if conta.numero == numero_conta:
                    conta_encontrada = conta
                    break

            if conta_encontrada:
                acesso_menu_transacoes(conta_encontrada)
            else:
                print("Conta não encontrada.")

        elif opcao == "2":  # Criar nova conta
            numero_conta = input("Digite o número da nova conta: ")
            conta_nova = Conta(cliente, numero_conta)
            cliente.adicionar_conta(conta_nova)
            print("Conta criada com sucesso!")

        elif opcao == "3":  # Listar contas do cliente
            for conta in cliente.contas:
                print(f"Agência: {conta.agencia}, Número: {conta.numero}")

        elif opcao == "9":  # Retorna ao menu_cliente
            return acesso_menu_cliente()

        elif opcao == "0":  # Fecha programa
            print("Obrigado por usar nossos Serviços!")
            break

        else:  # Opção inválida
            print("Operação inválida, por favor selecione uma opção disponível.")

def acesso_menu_cliente():
    clientes = []
    while True:
        opcao = menu_cliente()

        if opcao == "1":  # Acessar o cliente
            cpf = input("Informe o CPF: ")
            cliente_encontrado = None
            for cliente in clientes:
                if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
                    cliente_encontrado = cliente
                    break

            if cliente_encontrado:
                acesso_menu_conta(cliente_encontrado)
            else:
                print("Cliente não encontrado.")

        elif opcao == "2":  # Criar novo cliente
            cpf = input("Informe o CPF: ")
            nome = input("Informe o nome: ")
            data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
            endereco = input("Informe o endereço: ")

            novo_cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")

        elif opcao == "0":  # Encerra o programa
            print("Obrigado por usar nossos Serviços!")
            break

        else:
            print("Operação inválida, por favor selecione uma opção disponível.")

acesso_menu_cliente()
