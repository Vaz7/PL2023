import sys

def extract_numbers(text):
    # Cria uma lista vazia para armazenar as sequências de dígitos encontradas
    numbers = []
    current_number = ''
    
    # Loop que percorre cada caractere do texto
    for c in text:
        if c.isdigit():
            # Se o caractere é um dígito, adiciona-o à sequência atual
            current_number += c
        elif current_number:
            # Se o caractere não é um dígito, mas havia uma sequência em andamento,
            # adiciona-a à lista de sequências encontradas e reinicia a variável
            numbers.append(int(current_number))
            current_number = ''
    
    # Se ainda houver uma sequência em andamento no final do texto, adiciona-a à lista
    if current_number:
        numbers.append(int(current_number))
    
    return numbers

def somador():
    # Variável on/off
    on = True
    # Variável que armazena a soma das sequências de dígitos encontradas
    total = 0
    
    # Loop que lê cada linha do stdin
    for line in sys.stdin:
        # Remove espaços em branco do começo e fim da linha
        line = line.strip()
        
        # Verifica se a linha contém a string "Off" ou "On" em qualquer combinação de maiúsculas e minúsculas
        if line.lower() == "off":
            on = False
        elif line.lower() == "on":
            on = True
        else:
            # Se o comportamento está ligado, extrai as sequências de dígitos e as somas
            if on:
                numbers = extract_numbers(line)
                total += sum(numbers)
            # Se a linha contém o caractere "=", imprime o resultado da soma e zera a variável
            if "=" in line:
                print(total)
                total = 0

# Chama a função que implementa o comportamento descrito acima
somador()