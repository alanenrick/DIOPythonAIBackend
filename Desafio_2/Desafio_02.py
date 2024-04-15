import time
from decimal import Decimal

decimal_precision = Decimal('0.01')

saldo = Decimal('0')
limite = Decimal('500')
extrato = ""
quantidade_saques = 0
LIMITE_SAQUES = 3

menu = f"""
Seja bem vindo(a)!

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


Digite a opção desejada e telcle [Enter]
=> """

while True:
    
    opcao = input(menu)

    if opcao == "1":
            

        valor_deposito = Decimal(input("Informe o valor do depósito: R$ "))
        
        if valor_deposito > 0:
            
            saldo += valor_deposito
            
            extrato += f"{time.strftime('%d/%m/%y %X')}  |    Depósito   |  R$ {valor_deposito:.2f}\n"

            print(f"Depósito realizado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        com_saldo = saldo > 0

        if not com_saldo:
            print("Saque não disponível. Verifique seu saldo.")
        
        else:
            valor_saque = Decimal(input("Informe o valor do saque: R$ "))

            if 0 < valor_saque <= saldo and valor_saque <= limite and quantidade_saques < LIMITE_SAQUES:
            
                saldo -= valor_saque
            
                extrato += f"{time.strftime('%d/%m/%y %X')}  |    Saque      | (R$ {valor_saque:.2f})\n"
            
                quantidade_saques += 1
                
                print("Saque ralizado com sucesso!")
       
            else:
                print("Operação falhou! Verifique seu limite de saque ou quantidade de saques.")

    elif opcao == "3":

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

    elif opcao == "0":
        print(f"Obrigado por usar nossos Serviços!")
        break

    else:
        print("Operação inválida, por favor selecione uma opção disponível.")
    