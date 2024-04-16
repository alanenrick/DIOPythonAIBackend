import time
from decimal import Decimal

decimal_precision = Decimal('0.01')
usuarios = []
contas = []
LIMITE_SAQUES = 3


def filtrar_usuario(cpf, usuarios):
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n CPF já cadastrado, selecione a opção [Entra].")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nUsuário não encontrado, criação de conta encerrada!")

def filtrar_contas(cpf, contas):
    contas_filtradas = [conta for conta in contas if conta['usuario']['cpf'] == cpf]
    return contas_filtradas if contas_filtradas else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)   

def depositar(saldo, valor_deposito, extrato):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito:\tR$ {valor_deposito:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nValor de depósito inválido. O valor deve ser maior que zero.")


def sacar(*, saldo, valor_saque, extrato, limite, quantidade_saques, limite_saques):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite
    excedeu_saques = quantidade_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque:\t\tR$ {valor_saque:.2f}\n"
        quantidade_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    
    data_hora = time.localtime()
    data = time.strftime('%d/%m/%y',data_hora)
    hora = time.strftime('%H:%M:%S',data_hora)

    extrato_formatado = f"Não há registro de movimentações.\n" if not extrato else extrato
        
    saldo_formatado = f"Saldo em {data} {hora}:           R$ {saldo:.2f}"

    print("\n===================== EXTRATO =====================")
    print("\n===================================================")
    print("Data/Hora          |   Operação    |    Valor")
    print("===================================================")
    print(extrato_formatado)
    print(f"\n{saldo_formatado}")
    print("======================= FIM =======================")


def menu_usuarios():

    menu_usuarios = f'''
    Olá, seja bem vindo(a)!

    [1] Entrar
    [2] Criar usuário
    [0] Sair

    Digite a opção desejada e telcle [Enter]
    => '''
    return input(menu_usuarios)

def menu_contas():

    menu_contas = f'''
    Olá, ,

    [1] Acessar conta
    [2] Criar conta
    [3] Listar contas

    [9] menu de Usuários
    [0] Encerrar
    => '''
    return input(menu_contas)

def menu_operacoes():

    menu = f"""
    Olá, , Conta: 
        
    [1] Depositar
    [2] Sacar
    [3] Extrato

    [9] Menu de contas
    [0] Encerrar


    Digite a opção desejada e telcle [Enter]
    => """

    return input(menu)
    
def acesso_menu_operacoes():

    saldo = Decimal('0')
    limite = Decimal('500')
    extrato = ""
    quantidade_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []


    while True:
    
        opcao = input(menu_operacoes)

        if opcao == "1":
            
            valor_deposito = Decimal(input("Informe o valor do depósito: R$ "))
            
            saldo, extrato = depositar(saldo, valor_deposito, extrato)
            
        elif opcao == "2":
            com_saldo = saldo > 0

            if not com_saldo:
                print("Saque não disponível. Verifique seu saldo.")
        
            else:
                valor_saque = Decimal(input("Informe o valor do saque: R$ "))

                
                saldo, extrato = sacar(
                    saldo=saldo,
                    valor_saque=valor_saque,
                    extrato=extrato,
                    limite=limite,
                    quantidade_saques=quantidade_saques,
                    limite_saques=LIMITE_SAQUES,
                )

        elif opcao == "3":

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "9":
            print("Retornando ao menu de contas.")
            acesso_menu_contas()
        
        elif opcao == "0":
            print(f"Obrigado por usar nossos Serviços!")
            break

        else:
            print("Operação inválida, por favor selecione uma opção disponível.")
        


def acesso_menu_contas():

    while True:
        opcao = menu_contas()
    
        if opcao == '1':
        
            conta = input("Informe a conta: ")

            if conta in contas:
                acesso_menu_operacoes()

            else:
                print("Conta não encontrada, use uma conta valida ou crie uma conta!")    

        elif opcao == '2':
        
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '3':
            listar_contas(contas)


        elif opcao == '9':
            acesso_menu_usuarios()

        elif opcao == '0':
            break    

        else:
        
            print("Opção inválida, por favor selecione novamente uma opção válida.")



def acesso_menu_usuarios():
    
    while True:

        opcao = menu_usuarios()

        if opcao == '1':

            cpf = input("Digite o CPF do usuário: ")
            # usuario = filtrar_usuario(cpf, usuarios)

            # if usuario:
            acesso_menu_contas()

            # else:
               # print("usuario não encontrado, crie um usuário.")
               # acesso_menu_usuarios    

        elif opcao == '2':
            criar_usuario(usuarios)
    
            
        elif opcao == '0':
            break
    
        else:
            print("Opção inválida, por favor selecione novamente uma opção válida.")




acesso_menu_usuarios()
