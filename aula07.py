# Introdução às variáveis em Python

# Variáveis são usadas para armazenar informações que podem ser usadas e manipuladas ao longo do código.
# Em Python, não é necessário declarar o tipo da variável explicitamente; o interpretador infere o tipo com base no valor atribuído.
#PEP8 - Convenção de código para Python
# Nomes de variáveis devem ser descritivos e seguir certas regras:
# - Devem começar com uma letra (a-z, A-Z) ou um underscore (_)
# - Podem conter letras, números (0-9) e underscores (_)
# - Não podem conter espaços ou caracteres especiais (como !, @, #, etc.)
# - Devem ser escritos em letras minúsculas, com palavras separadas por underscores (snake_case)
# - Não devem ser palavras reservadas do Python (como if, else, while, etc.)

# Exemplos de nomes de variáveis válidos:
idade = 25
nome_completo = "João Silva"
altura_metros = 1.75
numero_de_telefone = "123456789"


# Exemplos de nomes de variáveis inválidos:
# 2idade = 30          # Começa com número
# nome-completo = "Maria"  # Contém hífen
# altura metros = 1.80  # Contém espaço
# if = 10              # Palavra reservada


# Exemplo de uso de variáveis
print("Nome:", nome_completo)
print("Idade:", idade)
print("Altura (m):", altura_metros)
print("Telefone:", numero_de_telefone)

# Podemos alterar o valor de uma variável a qualquer momento
idade = 26
print("Nova idade:", idade)

# Podemos usar variáveis em operações
ano_atual = 2024
ano_nascimento = ano_atual - idade
print("Ano de nascimento:", ano_nascimento)



