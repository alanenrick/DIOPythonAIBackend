import time
from decimal import Decimal, ROUND_HALF_UP

decimal_precision = Decimal('0.01')

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo1 = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

saldoinicial = Decimal(saldo1)



while True:

    opcao = input(menu)

    if opcao == "d":
        
        decimal_precision = Decimal('0.01')

        valordeposito = input("Informe o valor do depósito: ")
        
        valor = Decimal(valordeposito)


        data_hora = time.strftime('%d/%m/%y %X')

        if valor > 0:

            saldoinicial += valor

            extrato += f"{data_hora}|    Depósito   |   R$ {valor}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":

        decimal_precision = Decimal('0.01')

        valorsaque = input("Informe o valor do saque: ")
        valor = Decimal(valorsaque)

        excedeu_saldo = valor > saldoinicial

        excedeu_limite = valor > limite

        data_hora = time.strftime('%d/%m/%y %X')

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldoinicial -= valor
            extrato += f"{data_hora}|    Saque      |   R$ {valor}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":

        decimal_precision = Decimal('0.01')

        data_hora = time.localtime()
        data = time.strftime('%d/%m/%y',data_hora)
        hora = time.strftime('%H:%M:%S',data_hora)
        
        saldo = Decimal(saldoinicial)

        print("\n================ EXTRATO ================")
        print(f"Data: {data}          Horário: {hora}")
        print("==========================================")
        print("Data/Hora          |   Operação    |    Valor")
        print("==========================================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo}")
        print("===================FIM===================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
