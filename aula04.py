# Tipos de int e float
# int - números inteiros (positivos e negativos)
# O tipo int em Python suporta números inteiros de precisão ilimitada, limitado apenas pela memória disponível do sistema.
print(123456789012345678901234567890)  # Exemplo de int

# float - Números de ponto flutuante (números reais)
# O tipo float em Python é implementado usando a precisão dupla do padrão IEEE 754, o que significa que ele pode representar números com aproximadamente 15-17 dígitos decimais de precisão.
print(3.14159265358979323846)  # Exemplo de float

# A função type() mostra o tipo do dado
print( type(123))        # <class 'int'>
print( type(3.14))      # <class 'float'>
print( type("Olá"))    # <class 'str'>
print( type(2.3), type(2.3))   # <class 'float'>
