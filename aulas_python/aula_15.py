"""
Formatação basica de string

s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)

> - Esquerda
< - Direita
^ - Centro

Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}') #printou ABC
print(f'{variavel: >10}') #printou ABC com 7 espacos a esquerda.
print(f'{variavel: <10}') #printou ABC com 7 espacos a direita.
print(f'{variavel: ^10}') #printou o valor da variavel centralizado (totalizando 10 espacos).
print(f'{variavel:#^10}') #printou o valor da variavel centralizado preenchendo as reservas de espacos com o caractere escolhido (totalizando 10 espacos).
print(f'{1000.87767565656: .1f}') #printou 1000.87767565656 com apenas 1 casa decimal.
print(f' O valor hexadecimal de 1500 é {1500:08x}') #printou o valor hexadecimal de 1500 prenchendo os espacos faltantes de 8 caracteres com o numero 0.



