# Definindo o faturamento mensal por estado
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calculando o faturamento total
total_faturamento = sum(faturamento.values())

# Calculando e exibindo o percentual de representação de cada estado
print("Percentual de representação do faturamento mensal por estado:")
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100  # Cálculo do percentual
    print(f"{estado}: {percentual:.2f}%")

