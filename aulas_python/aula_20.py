"""
Flag (Bandeira) - Marcar um local
None = Nãp valor
is e is not = é ou não é (tipo, valor, identidade)

id = identidade
"""

#o python consegue identificar o valor literal, e acaba retornando o mesmo id do espaço da. 
v1 = 'a' 
v2 = 'a'


#OBS : IMUTAVEIS QUE VIMOS: str, int, float e bool

string = "João Bispo"
variavel_1 = f'{string[:5]}HELLO{string[4:]}' 
"""
como mencionado acima, as strings são imutaveis, caso vc queira muda-las ou manipular o seu valor de alguma forma,
voce pode utilizar o .format, conforme o exeplo acima. onde ele pega os valores do inicio até o indice 5, acrecenta 
o valor HELLO e concatena com tudo que vier a partir do indice 4 
"""

print(variavel_1)