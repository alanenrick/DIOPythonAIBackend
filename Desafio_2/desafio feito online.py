import time
from decimal import Decimal

decimal_precision = Decimal('0.01')
saldo = Decimal('0')
limite = Decimal('500')
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

AGENCIA = "0001"

def filtrar_usuario(cpf, usuarios):    # Verificar se usuário exite
    
    usuario_encontrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    
    return usuario_encontrado[0] if usuario_encontrado else None

def criar_usuario(usuarios):    # Criar usuário
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:    # Não permite duplicidade de usuários
        print("\n CPF já cadastrado, selecione a opção [Entra].")
        return

    else:    # Continuar criando usuário
        nome = input("Informe seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento(dd-mm-aaaa): ")
        endereco = input("Informe seu endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

        print("Usuário criado com sucesso!")
        return


def criar_conta(agencia, conta_cc, usuarios):    # Criar conta corrente
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario: # Vincula a conta a um usuário
        print("\n Conta corrente criada com sucesso!")
        return {"agencia": AGENCIA, "conta_cc": conta_cc, "usuario": usuario}
    
    else:
        print("\nUsuário não encontrado, criação de conta encerrada!")


# def filtrar_contas(cpf, contas):    # Verificar se a conta existe
    # conta_encontrada = [conta_cc for conta_cc in contas if conta_cc['usuario']['cpf'] == cpf]
    # return conta_encontrada if conta_encontrada else None

def filtrar_contas(cpf, contas):    # verificar se a conta existe
    if conta_cc:
        print(f"Contas de {usuario}:")
        for conta_cc in contas:
            print(f"-C/C: {conta_cc['conta_cc']}")

    else:
        print("Usuário não possui contas cadastradas.")


def listar_contas(contas):    # Exibir lista de contas
    for conta_cc in contas:
        linha = f"""\
            Agência:\t{conta_cc['agencia']}
            C/C:\t\t{conta_cc['conta_cc']}
            Titular:\t{conta_cc['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)   

def depositar(saldo, valor_deposito, extrato):    # Operação de depósito
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Depósito   |  R$ {valor_deposito:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nValor de depósito inválido. O valor deve ser maior que zero.")


def sacar(*, saldo, valor_saque, extrato, limite, quantidade_saques, limite_saques):    # Operação de saque
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
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Saque      | (R$ {valor_saque:.2f})\n"
        quantidade_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):    # Operação de exibição de extrato
    
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


def menu_usuarios(): # Primeiro menu para criar ou acessar um usuário existente

    menu_usuarios = f'''
    Olá, seja bem vindo(a)!

    [1] Entrar
    [2] Criar usuário
    [0] Sair

    Digite a opção desejada e telcle [Enter]
    => '''
    return input(menu_usuarios)

def menu_contas():    # Segundo menu para Criar, Acessar ou Listar contas

    menu_contas = f'''
    Olá, ,

    [1] Acessar conta corrente
    [2] Criar conta corrente
    [3] Listar contas

    [9] menu de Usuários
    [0] Encerrar
    
    Digite a opção desejada e telcle [Enter]
    => '''
    return input(menu_contas)

def menu_operacoes():    # Terceiro menu para realizar as operações de Depósito, Saque e Extrato

    menu_operacoes = f'''
    Olá, , Conta: 
        
    [1] Depositar
    [2] Sacar
    [3] Extrato

    [9] Menu de contas
    [0] Encerrar


    Digite a opção desejada e telcle [Enter]
    => '''

    return input(menu_operacoes)
    
def acesso_menu_operacoes():    # Acesso ao terceiro menu

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
        


def acesso_menu_contas():    # Acesso ao segundo menu

    while True:
        opcao = menu_contas()
    
        if opcao == '1':
        
            conta_cc = input("Informe a conta: ")

            if conta_cc:
                print("Acessando a conta.")
                acesso_menu_operacoes()

            else:
                print("Conta não encontrada, use uma conta valida ou crie uma conta!")    

        elif opcao == '2':
        
            conta_cc = len(contas) + 1
            conta_cc = criar_conta(AGENCIA, conta_cc, usuarios)

            if conta_cc:
                contas.append(conta_cc)

        elif opcao == '3':
            listar_contas(contas)


        elif opcao == '9':
            acesso_menu_usuarios()

        elif opcao == '0':
            break    

        else:
        
            print("Opção inválida, por favor selecione novamente uma opção válida.")



def acesso_menu_usuarios():    # Acesso ao primeiro menu
    
    while True:

        opcao = menu_usuarios()

        if opcao == '1':

            cpf = input("Digite o CPF do usuário: ")
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                acesso_menu_contas()

            else:
                print("usuario não encontrado, crie um usuário.")
                acesso_menu_usuarios()    

        elif opcao == '2':
            criar_usuario(usuarios)
    
            
        elif opcao == '0':
            break
    
        else:
            print("Opção inválida, por favor selecione novamente uma opção válida.")




acesso_menu_usuarios()    # Start no programa
