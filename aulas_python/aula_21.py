"""
Faça um programa que peça ao usuario para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuario não digite u número
inteiro, informe que não é um numero inteiro
"""

print("========== SISTEMA 1 ==========")
nome = input("Olá, me chamo Bispo, Qual é o seu nome ? ... ")
numero = input(f'{nome}, Digite um numero sem pontos ou virgulas...')

try:
    numero_int = int(numero)  
    if numero_int % 2 == 0:
        print(f'{nome}, o valor que voce digitou "{numero_int}" é um número PAR')
    elif numero_int % 2 == 1:
        print(f'{nome}, o valor que voce digitou "{numero_int}" é um número ÍMPAR')   
except:
   print(f'{nome}, o valor que voce digitou " {numero} " não é um número inteiro')

"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
"""

print("========== SISTEMA 2 ==========")
nome = input("Olá, me chamo Bispo, Qual é o seu nome ? ... ")
horas = input(f'{nome}, que horas são ? ')

try:
    horas_int = int(horas)
    if horas_int >= 0 and horas_int <=11:
        print(f'{nome}, Bom dia!')
    elif horas_int >= 12 and horas_int <= 17:
        print(f'{nome}, Boa tarde!')
    elif horas_int >= 18 and horas_int <= 23:
        print(f'{nome}, Boa noite!')
    else:
        print(f'{nome}, esse horário não existe!')
except:
    print(f'{nome}, voce não digitou um horario valido')

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos
escreva "seu nome é curto"; se tiver entre 5 e 6 letras, escreva "seu nome é normal";
maior que 6 letras "seu nome é muito grande".
"""

print("========== SISTEMA 3 ==========")
nome = input("Olá, me chamo Bispo GPT, Qual é o seu nome ? ... ")
quantidade_letras = len(nome)
if quantidade_letras > 1:
    if ' ' in nome:
        print("digite apenas o primeiro nome!")
    elif quantidade_letras <= 4:
        print(f'{nome}, seu nome é curto. Composto por {quantidade_letras} letras!')
    elif quantidade_letras >= 5 and quantidade_letras <= 6:
        print(f'{nome}, seu nome é normal. Composto por {quantidade_letras} letras!')
    else:
        print(f'{nome}, seu nome é muito grande. Composto por {quantidade_letras} letras!')
else:
    print("Digite mais de uma letra!")