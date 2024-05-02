import time     # Importar data e hora
from decimal import Decimal     # Importar tipo de dado numérico decimal
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod      # Importar ABC     

class Cliente:      # Cria Classe cliente
    def __init__(self, endereco): 
        self.endereco = endereco
        self.contas = []
        
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta, transacao)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)
        
    def len_contas(self):
        return len(self.contas)
        
class PessoaFisica(Cliente):        # Cria Classe pessoa fisica derivado de cliente
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        
class Conta:        # Criar Classe Conta 
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
    
    def sacar(self, valor):       # Função sacar, dentro de Conta       
        if valor > self.saldo:
            print("Operação Faalhou! Saldo insuficiente!")
            return False
        else:
            self._saldo -= valor
            return True
        
    def depositar(self, valor):        # Função depositar, dentro de Conta        
        if valor > 0:
            self._saldo += valor
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False
        
    def novo_numero(self, cliente):
        return self._cliente.len_contas() + 1
class ContaCorrente(Conta):     # Criar objeto conta corrente derivado de Conta    
    def __init__(self, cliente, numero):
        super().__init__(cliente, numero)
        self.limite = Decimal("500.00")
        self.LIMITE_SAQUES = 0
        self.quantidade_saques = 0
        
        
    def sacar(self, valor):       # Função sacar derivado de Conta, dentro de Conta Corrente
        limite_excedido = valor > self.limite
        saques_excedidos = self.quantidade_saques >= self.LIMITE_SAQUES
        
        if limite_excedido:
            print("Transação Falhou! Limite excedido!")
            return False
        
        elif saques_excedidos:
            print("Transação Falhou! Limite de saques excedidos!")
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
                "data": time.localtime('%d/%m/%y' '%H:%M:%S'),
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
        print(f"Depósito realizado com sucesso!")
    
    else:
        print("Operação falhou! O valor informado é inválido.")

        
def sacar (valor, conta):
    if valor > 0:
        Saque(valor).registrar(conta)    
        print("Saque ralizado com sucesso!")
       
    else:
        print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")

            
def exibir_extrato(conta):
    historico = conta.historico.transacoes
    data_hora = time.localtime()
    data = time.strftime('%d/%m/%y',data_hora)
    hora = time.strftime('%H:%M:%S',data_hora)

    if historico:
        extrato_formatado = historico
        
    else:
        extrato_formatado = [{"Não há registo de movimentações."}]
        
    saldo_formatado = f"\nSaldo em {data} {hora}:           R$ {conta.saldo:.2f}"

    print("\n===================== EXTRATO =====================")
    print("\n===================================================")
    print("Data/Hora          |   Operação    |    Valor")
    print("===================================================")
    for transacao in extrato_formatado:
        print(f"{transacao['data']}  |  {transacao['tipo']}  |  R$ {transacao['valor']:.2f}")
    print(saldo_formatado)
    print("======================= FIM =======================")
        

def filtrar_cliente(clientes, cpf):
    cliente_existente = next((cliente for cliente in clientes if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf), None)
    if cliente_existente:
        return cliente_existente
    else:
        return False

def verificar_conta(cliente, numero_conta):
    for conta in cliente.contas:
        if conta.numero == numero_conta:
            return conta
    return None

def verifica_saldo(conta):
    return conta.saldo > 0

def menu_cliente():
    menu_cliente = f"""
    
    Seja bem vindo(a)!
    
    [1] Entrar
    [2] Cadastrar Cliente
    
    [0] Sair
    
    Digite a opção desejada e telcle [Enter]
    => """
    return input(menu_cliente)

def menu_conta():
    menu_conta = f"""
    [1] Acessar conta
    [2] Criar conta
    [3] Listar contas
    
    [0] Sair
    
    Digite a opção desejada e telcle [Enter]
    => """
    return input(menu_conta)

def menu_transacoes():     # Função exibir menu

    menu_transacoes = f"""

    [1] Depositar
    [2] Sacar
    [3] Extrato
    
    [0] Sair

    Digite a opção desejada e telcle [Enter]
    => """
    return input(menu_transacoes)

cliente_padrao = PessoaFisica("Rua a, 1 - bairro a - cidade a/BA", "12345678900", "Alan Henrique", "02-05-2024")        # Criado usuário padrão, para agilizar meus testes
conta_padrao = Conta(cliente_padrao, "001")     # Criada conta padrão com número "001" ,para facilitar meus testes.
cliente_padrao.adicionar_conta(conta_padrao)


def acesso_menu_transacoes(conta):      # Função acessar menu
    while True:
        opcao = menu_transacoes()

        if opcao == "1":        # Depositar  
            valor = Decimal(input("Informe o valor do depósito: R$ "))
            depositar(conta, valor)

        elif opcao == "2":      # Sacar
            com_saldo = verifica_saldo(conta)
            if not com_saldo:   
                print("Saque não disponível. Verifique seu saldo.")

            else :
                valor = Decimal(input("Informe o valor do saque: R$ "))
                sacar(valor, conta)
            
        elif opcao == "3":      # Exibir extrato
            exibir_extrato(conta)
             
        elif opcao == "9":      # voltar para menu_conta
            print("Voltando ao menu de Contas")
            return acesso_menu_conta()
        
        elif opcao == "0":      # Fechar programa
            print(f"Obrigado por usar nossos Serviços!")
            break

        else:       # opção inválida
            print("Operação inválida, por favor selecione uma opção disponível.")
            
def acesso_menu_conta(cliente):
    while True:
        opcao = menu_conta()
        if opcao == "1":        # Acessar menu transações da conta
            numero_conta = input("Digite o número da conta: ")
            conta_encontrada = verificar_conta(cliente, numero_conta)

            if conta_encontrada:
                acesso_menu_transacoes(conta_encontrada)
            else:
                print("Conta não encontrada.")
        
        elif opcao == "2":      # Criar nova conta
        
            numero_conta = cliente.len_contas() + 1
            conta_nova = Conta(cliente, str(numero_conta))
            cliente.adicionar_conta(conta_nova)
            print("Conta criada com sucesso!")
            
        elif opcao == "3":      # Listar contas do cliente
            for conta in cliente.contas:
                print(f"Agência: {conta.agencia}, Número: {conta.numero}")
        
        elif opcao == "9":      # Retorna ao menu_cliente
            return acesso_menu_cliente()        
        
        elif opcao == "0":      # Fecha programa
            print(f"Obrigado por usar nossos Serviços!")
            break
            
        else:       # opção inválida
            print("Operação inválida, por favor selecione uma opção disponível.")
                
def acesso_menu_cliente():
    clientes = [cliente_padrao]
    while True:
        opcao = menu_cliente()
        
        if opcao == "1":        # Acessar o cliente
            cpf = input("Informe o CPF: ")
            cliente_existente = filtrar_cliente(clientes, cpf)
            if cliente_existente:
                cliente = cliente_existente
                acesso_menu_conta(cliente)
                
            else:
                print("Cliente não encontrado!")
                
        elif opcao == "2":      # Criar novo cliente
            cpf = input("Informe o CPF (somente números): ")
            cliente_existente = filtrar_cliente(clientes, cpf)
            if cliente_existente:
                print("Já existe um cliente com esse CPF.")
                return acesso_menu_cliente()
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

            novo_cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
            clientes.append(novo_cliente)
            print("Cliente cadastrado com sucesso!")
            
        elif opcao == "0":      # Encerra o programa
            print(f"Obrigado por usar nossos Serviços!")
            break

        else:
            print("Operação inválida, por favor selecione uma opção disponível.")

        
            
acesso_menu_cliente()
