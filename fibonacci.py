# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


# Função para verificar se um número pertence à sequência de Fibonacci
def pertence_fibonacci(num):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    
    # Gera a sequência de Fibonacci até que o número atual seja maior ou igual ao número informado
    while b <= num:
        # Se o número atual for igual ao número informado, retorna True
        if b == num:
            return True
        # Atualiza os valores para o próximo número da sequência
        a, b = b, a + b
    
    # Se a sequência ultrapassou o número informado sem encontrá-lo, retorna False
    return False

# Função principal para verificar uma lista de números
def verificar_lista_fibonacci(numeros):
    for num in numeros:
        # Chama a função para verificar se o número pertence à sequência de Fibonacci
        if pertence_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} NÃO pertence à sequência de Fibonacci.")

# Lista de números para verificar (alguns são Fibonacci, outros não)
numeros = [2, 4, 5, 7, 8, 13, 20, 21, 34, 40]

# Chama a função principal para verificar os números na lista
if __name__ == "__main__":
    verificar_lista_fibonacci(numeros)

