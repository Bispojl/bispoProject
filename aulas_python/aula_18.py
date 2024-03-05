"""
Introdução ao try/except
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
"""

#nao é recomendado utilzar dessa maneira, mas vai ser util para uma pequena introdução.

numero_str = input('vou dobrar o numero que voçe digitar :')

try:
    numero_float = float(numero_str)
    print("FLOAT", numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.1f}')
except:
    print("isso não é um número!")