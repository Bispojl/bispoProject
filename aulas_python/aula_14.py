"""
Interpolacao basica de string

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF1234567890)
"""

nome = 'bispo'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %x' % (1500, 1500))
