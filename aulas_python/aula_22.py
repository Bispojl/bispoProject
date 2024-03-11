"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira.
"""

condicao = True

while condicao:
    nome = input("Qual o seu nome ?")
    print(f'seu nome é: {nome}')

    if nome == 'sair' or nome == "Sair":
        break

print("fim de codigo.")

"""
while + concatenação
"""

contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1

print("fim de codigo.")

"""
Operadores de atribuição
=  +=  *=  /=  //=  **=  %=

exemplo : 
contador += 2
contador -= 1
"""

contador = 0

while contador <= 10:
    print(contador)
    contador += 2

print("fim de codigo.")

"""
utilizando o continue
"""

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("não vou mostrar o", contador)
        continue

    if contador >= 10 and contador <= 30:
        print("não vou mostrar o ", contador)
        continue
    
    print(contador)

    if contador == 40:
        break