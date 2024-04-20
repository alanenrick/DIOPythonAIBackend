import time
from decimal import Decimal

decimal_precision = Decimal('0.01')

def menu():

    menu = f"""
    Seja bem vindo(a)!

    [1] Depositar
    [2] Sacar
    [3] Extrato
    
    [4] Nova conta
    [5] Listar contas
    [6] Novo usuário
    
    [0] Sair


    Digite a opção desejada e telcle [Enter]
    => """
    return input(menu)

def depositar(saldo, extrato):

    valor_deposito = Decimal(input("Informe o valor do depósito: R$ "))
        
    if valor_deposito > 0:
            
        saldo += valor_deposito
            
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Depósito   |  R$ {valor_deposito:.2f}\n"

        print(f"Depósito realizado com sucesso!")
        
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(saldo, extrato, quantidade_saques, limite, LIMITE_SAQUES):
    
    valor_saque = Decimal(input("Informe o valor do saque: R$ "))

    if 0 < valor_saque <= saldo and valor_saque <= limite and quantidade_saques < LIMITE_SAQUES:
            
        saldo -= valor_saque
            
        extrato += f"{time.strftime('%d/%m/%y %X')}  |    Saque      | (R$ {valor_saque:.2f})\n"
            
        quantidade_saques += 1
                
        Print("Saque ralizado com sucesso!")
       
    else:
        print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")

def exibir_extrato(saldo, extrato):

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

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("\nInforme o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\nCPF vinculado a um usuário existente.")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    
    print("Usuário criado com sucesso!")     
        

def criar_conta(agencia, numero_conta, usuarios):
    numero_conta = len(contas) + 1 # Retirar caso gere falha
    cpf = input("Informe o CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    agencia = AGENCIA
    
    if usuario: # Modificar caso gere falha
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("\nConta: {numero_conta}, criada com sucesso!!!") 
    
    else:
        print("Usuário não encontrado. Use um usuário válido ou crie um novo.")        

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
        
                
def main():
    
    decimal_precision = Decimal('0.01')
    saldo = Decimal('0')
    limite = Decimal('500')
    extrato = ""
    quantidade_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
    
        opcao = menu()

        if opcao == "1":    # Função depositar
            depositar(saldo, extrato)

        elif opcao == "2":  # Função sacar
            com_saldo = saldo > 0

            if not com_saldo:
                print("Saque não disponível. Verifique seu saldo.")

            else :
                sacar(saldo, extrato, quantidade_saques, limite, LIMITE_SAQUES)
            
        elif opcao == "3":  # Função exibir extrato
            exibir_extrato(saldo, extrato)

        elif opcao == "4":  # Função nova conta
            criar_conta(agencia, numero_conta, usuarios)    # Caso gere falhas, fazer alteração
            
        elif opcao == "5":  # Função listar contas
            listar_contas(contas)
                    

        elif opcao == "6":
            criar_usuario(usuarios)
                    
        elif opcao == "0":
            print(f"Obrigado por usar nossos Serviços!")
            break

        else:
            print("Operação inválida, por favor selecione uma opção disponível.")
            
main()