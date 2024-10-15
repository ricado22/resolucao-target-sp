import json

# Função para carregar os dados do faturamento a partir de um arquivo JSON
def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados['faturamento']

# Função para calcular o menor, maior e a média do faturamento
def analisar_faturamento(faturamento):
    valores = [valor for valor in faturamento.values() if valor > 0]  # Ignorar dias sem faturamento
    
    if not valores:
        return None, None, 0  # Retornar None se não houver faturamento

    menor = min(valores)  # Menor valor
    maior = max(valores)  # Maior valor
    media = sum(valores) / len(valores)  # Média dos dias com faturamento
    
    # Contar dias com faturamento superior à média
    dias_superior_media = sum(1 for valor in valores if valor > media)
    
    return menor, maior, dias_superior_media

# Função principal
def main():
    arquivo = 'faturamento.json'  # Nome do arquivo JSON com os dados de faturamento
    faturamento = carregar_faturamento(arquivo)  # Carregar faturamento
    menor, maior, dias_superior_media = analisar_faturamento(faturamento)  # Analisar faturamento

    # Exibir resultados
    print(f'Menor faturamento: R$ {menor:.2f}')
    print(f'Maior faturamento: R$ {maior:.2f}')
    print(f'Dias com faturamento superior à média: {dias_superior_media}')

if __name__ == '__main__':
    main()
