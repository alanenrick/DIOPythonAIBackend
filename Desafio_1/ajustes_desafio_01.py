import time
from decimal import Decimal

decimal_precision = Decimal('0.01')
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = Decimal('0')
limite = Decimal('500')
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = Decimal(input("Informe o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"{time.strftime('%d/%m/%y %X')} |    Depósito   |   R$ {valor_deposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor_saque = Decimal(input("Informe o valor do saque: "))
        if 0 < valor_saque <= saldo and valor_saque <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor_saque
            extrato += f"{time.strftime('%d/%m/%y %X')} |    Saque      |   R$ {valor_saque:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! Verifique seu saldo, limite de saque ou número de saques.")

    elif opcao == "e":
        data_hora = time.strftime('%d/%m/%y %X')
        extrato_formatado = f"{data_hora} | Operação | Valor\n" if not extrato else extrato
        saldo_formatado = f"Saldo: R$ {saldo:.2f}"
        print("\n================ EXTRATO ================")
        print("Data/Hora          |   Operação    |    Valor")
        print("==========================================")
        print(extrato_formatado)
        print(f"\n{saldo_formatado}")
        print("===================FIM===================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
