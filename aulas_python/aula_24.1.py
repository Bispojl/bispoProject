nome = input("Olá, Qual o seu nome ?  ")
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(f'Bem vindo {novo_nome} !!!')