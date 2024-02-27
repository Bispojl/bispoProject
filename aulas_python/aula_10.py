# Operadores de comparacao ( relacionais )
# OP                SIGNIFICADO               EXEMPLO
# >                 maior                     2 > 1      
# >=                maior ou igual            2 >= 2
# <                 menor                     1 < 2
# <=                menor ou igual            2 <= 2
# ==                igual                     'a' == 'a'
# !=                diferente                 'a' != 'b'

# maior =  2 > 1  
# maior_igual = 2 >= 2
# diferente = 'a' != 'b'

#python3 -i "nome do modulo python, testa via terminal em tempo real, passando as variaiveis"
#quit() ou exit() para sair da execucao

primeiro_valor = input("digite um valor: ")
segundo_valor = input("digite outro valor: ")

if primeiro_valor > segundo_valor:
    print(primeiro_valor + " é maior que " + segundo_valor)
elif primeiro_valor < segundo_valor:
    print(primeiro_valor + " é menor que " + segundo_valor)
else:
    print(primeiro_valor + " e " + segundo_valor + " sao iguais")
print()
print()

# ou utilizando o o f'string 

primeiro = input("digite um valor: ")
segundo = input("digite outro valor: ")

if primeiro > segundo:
    print(f'{primeiro} é maior que o {segundo}')
elif primeiro < segundo:
    print(f'{primeiro} é menor que o {segundo}')
else:
    print(f'{primeiro} e o {segundo} sao iguais')