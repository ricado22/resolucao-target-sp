# Definindo a string (você pode trocar por uma entrada do usuário, se preferir)
string_original = "Música da xuxa"

# Função para inverter a string
def inverter_string(string):
    string_invertida = ""
    
    # Percorre a string do último caractere até o primeiro
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]  # Adiciona cada caractere ao resultado
    
    return string_invertida

# Exibindo o resultado
print("String original:", string_original)
print("String invertida:", inverter_string(string_original))
