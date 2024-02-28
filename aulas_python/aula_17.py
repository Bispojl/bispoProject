"""
Exercicio
Peca ao usuario para digitar seu nome
Peca ao usuario para digitar sua idade
Se nome e idade forem digitados:

    Exiba:
        seu nome é :
        seu nome invertido é:
        seu nome contem (ou nao) espaços:
        seu nome tem n letras:
        a primeira letra do seu nome é:
        a ultima letra do seu nome é:
Se nada for digitado em nome ou idade:
    Exiba:
        desculpe, voce deixou campos vazios.
"""

nome = input("Qual o seu nome ? ")
idade = input("quantos anos voce tem ? ")

if not nome or not idade:
    print("desculpe, voce deixou campos vazios")
else:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print(f'seu nome {nome}, possui espaços')
    else:
        print(f'seu nome {nome}, não possui espaços.')
    print(f'seu nome {nome}, tem uma quantidade de: {len(nome)} letras')
    print(f'a primeira letra do seu nome {nome} é: {nome[:1]}')
    print(f'a ultima letra do seu nome {nome} é: {nome[-1:]}')

##### outra forma de fazer 
    
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")


