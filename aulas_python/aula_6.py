"""
Variaveis sao usadas para salvar algo na memoria do computador.
PIP8: inicia variaveis com letras minusculas, pode usar numeros e _.
O sinal de = é utilizado para atribuição, usado para atribuir um valor
a uma variavel.

uso : nome_variavel = expressão
"""

# nome_completo = 'Joao Luis Bispo Jr'
# soma_valores = 5 + 5
# print(nome_completo, soma_valores, sep=' = ')

nome = "Junior"
sobre_nome = "Bispo"
idade = 27
ano_nascimento = 1996
maior_idade = idade >= 18
altura_metros = 1.76

print("nome: " + nome, "idade: " + str(idade), "maior de idade: " + str(maior_idade), sep=" -- ")
print("nome:", nome, type(nome))
print("sobrenome:", sobre_nome, type(sobre_nome))
print("idade:", idade, type(idade))
print("ano de nascimento:", ano_nascimento, type(ano_nascimento))
print("maior de idade:", maior_idade, type(maior_idade))
print("altura:", altura_metros, type(altura_metros))


adicao = 10 + 10
print("Adição:", adicao)

subtracao = 10 - 5
print("subtração:", subtracao)

multiplicacao = 10 * 10
print("multiplicação:", multiplicacao)

divisao = 10 / 3  #float
print("divisão", divisao)

divisao_inteira = 10 // 3
print("divisão inteira:", divisao_inteira)

exponenciacao = 2 ** 10
print("exponenciação:", exponenciacao)

modulo = 55 % 2  #retorna o resto da divisão
print("modulo", modulo)