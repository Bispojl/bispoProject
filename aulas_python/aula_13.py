'''
Operadores IN e NOT IN 
Strings sao interaveis ou seja o python percorre 
por toda stringpara devolver um resultado

0 1 2 3 4 5
J U N I O R

'''

nome = "junior"
print(nome[3])  #ele ira retornar a letra do indice 3

print('jun' in nome) # caso contenha a plavra 'jun' na variavel nome, o python ira retornar true
print(10 * '-')
print('jun' not in nome) # se nao houver a palavra 'jun na variavel nome, o pyhton ira retornar true.

nomeE = input('Qual o seu nome ? ')
chave = input('Oque voce deseja encontrar ? ')

if chave in nomeE:
    print(f'a palavra {chave} esta entre {nomeE}')
else:
    print(f'nao encontramos a palavra {chave} no {nomeE}')