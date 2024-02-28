"""
Fatiamento de strings
012345678
Ola mundo

Fatiamento [inicio:fim:passo] [::]

Obs: a função len retorna a quantidade 
de caracteres da variavel
"""

variavel = 'Olá mundo'

print(variavel[:5])
#fatiando a variavel e retornando o valor que esta do inicio até o indice 4.

print(len(variavel)) 
#retornar a quantidade de caracteres dentro da variavel.

print(len(variavel[3:7])) 
#fatiando a variavel com ponto de inicio do indice 3 e termino no indice 6 pois o ultimo nao conta. Alem de  
#retorna a quantidade de caracteres dentro do fatiamento.

print(variavel[0:9:2]) #fatiando no inicio ate o final da variavel e pegando os caracteres em 2 em 2 
print(variavel[:len(variavel):2]) #mesma coisa que o passo de cima
