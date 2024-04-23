# Verificador de planos de internet
import sys
# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo):
  if 0 <= consumo <= 10:
    return "Plano Essencial Fibra - 50Mbps."
        
  elif 10 < consumo <= 20:    
    return "Plano Prata Fibra - 100Mbps."
    
  elif 20 < consumo:
    return "Plano Premium Fibra - 300Mbps."
        
  else:
    return f"Consumo informado é invalido, são aceitos apenas numeros positivos "

    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(sys.stdin.readline())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))