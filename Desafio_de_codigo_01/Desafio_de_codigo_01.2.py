# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":
def solicita_itens(itens):
    item = input()
    itens.append(item)
    
def main():
    itens = []
    contagem = 0
    while contagem < 3:
        solicita_itens(itens)
        contagem += 1
        
    # Exibe a lista de itens
    print("Lista de Equipamentos:")  
    for item in itens:
    # Loop que percorre cada item na lista "itens"
        print(f"- {item}")
        
main()


