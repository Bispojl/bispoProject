"""
interando string com while
"""

# string são interaveis, ou seja elas possuem posições em vetores (indices)

nome = 'JOÃO BISPO'
#.......12345678910

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
    
novo_nome += '*'
print(novo_nome)