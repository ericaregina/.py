# Função para calcular a média de uma lista de vendas
def calcular_media_vendas(vendas):
    if not vendas:
        return 0  # Retorna 0 se a lista estiver vazia
    
    total_vendas = sum(vendas)
    numero_de_vendas = len(vendas)
    media_vendas = total_vendas / numero_de_vendas
    
    return media_vendas

# Lista de vendas
vendas = [100, 200, 150, 300, 250]

# Calculando a média
media = calcular_media_vendas(vendas)

# Exibindo o resultado
print(f"A média de vendas é: {media:.2f}")
