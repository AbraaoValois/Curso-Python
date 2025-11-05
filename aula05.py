# tipo de dados booleano
# ao questionar algo em Python, a resposta pode ser True (verdadeiro) ou False (falso)
# só existem esses dois valores no tipo booleano:
# sim (true) ou não (false).
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que questiona se um valor é igual a outro valor.
print( 10 == 10 )   # True, pois 10 é igual a 10
print( 10 == 5 )    # False, pois 10 não é igual a 5
print( 3.14 == 3.14 )  # True, pois 3.14 é igual a 3.14
print( 3.14 == 2.71 )  # False, pois 3.14 não é igual a 2.71
print( "Olá" == "Olá" )  # True, pois as strings são iguais
print( "Olá" == "olá" )  # False, pois as strings são diferentes (case-sensitive)
print( type(10 == 10) )  # <class 'bool'>
print( type(10 == 5) )   # <class 'bool'>
print( type("Olá" == "Olá") )  # <class 'bool'>
print( type("Olá" == "olá") )  # <class 'bool'>
