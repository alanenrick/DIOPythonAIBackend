import time
from decimal import Decimal

usuarios = []
contas = []
limite_saques = 3

def criar_usuario():
    cpf = input("Informe o CPF (somente números): ")
    if filtrar_usuario(cpf):
        print("CPF já cadastrado.")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço: ")
    usuarios.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf):
    return next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

def criar_conta():
    cpf = input("Informe o CPF do titular da conta: ")
    usuario = filtrar_usuario(cpf)
    if not usuario:
        print("Usuário não encontrado.")
        return
    agencia = input("Informe a agência da conta: ")
    numero_conta = len(contas) + 1
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": Decimal("0")}
    contas.append(conta)
    print("Conta criada com sucesso!")

def menu_principal(usuario):
    print(f"Olá, {usuario['nome']}, Conta: {usuario['conta']}")
    while True:
        opcao = input("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
        Digite a opção desejada: """)
        if opcao == "1":
            depositar(usuario)
        elif opcao == "2":
            sacar(usuario)
        elif opcao == "3":
            extrato(usuario)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

def depositar(usuario):
    valor_deposito = Decimal(input("Informe o valor do depósito: "))
    if valor_deposito > 0:
        usuario["saldo"] += valor_deposito
        registrar_transacao(usuario, "Depósito", valor_deposito)
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")

def sacar(usuario):
    if usuario["saldo"] > 0:
        valor_saque = Decimal(input("Informe o valor do saque: "))
        if 0 < valor_saque <= usuario["saldo"]:
            usuario["saldo"] -= valor_saque
            registrar_transacao(usuario, "Saque", valor_saque)
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido.")
    else:
        print("Saldo insuficiente.")

def extrato(usuario):
    print("Extrato:")
    for transacao in usuario["transacoes"]:
        print(transacao)
    print(f"Saldo atual: R$ {usuario['saldo']:.2f}")

def registrar_transacao(usuario, tipo, valor):
    transacao = f"{time.strftime('%d/%m/%y %X')} | {tipo} | R$ {valor:.2f}"
    usuario.setdefault("transacoes", []).append(transacao)

def main():
    while True:
        opcao = input("""
        [1] Entrar
        [2] Criar usuário
        [3] Criar conta
        [0] Sair
        Digite a opção desejada: """)
        if opcao == "1":
            cpf = input("Digite seu CPF: ")
            usuario = filtrar_usuario(cpf)
            if usuario:
                menu_principal(usuario)
            else:
                print("Usuário não encontrado.")
        elif opcao == "2":
            criar_usuario()
        elif opcao == "3":
            criar_conta()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")

main()
