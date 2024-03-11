""" Calculadora com while """

while True:
    numero_1 = input("Digite o primeiro numero: ")
    numero_2 = input("Digite o segundo numero: ")
    operador = input("digite o operador (+ - / *): ")
    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("um ou ambos os numeros digitados, são invalidos")
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print("Este operador não é valido.")
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue
    
    print("REALIZANDO A SUA CONTA...")

    if operador == '+':
        print(f'{numero_1_float} + {numero_2_float} = ', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - {numero_2_float} = ', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * {numero_2_float} = ', numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / {numero_2_float} = ', numero_1_float / numero_2_float)

    sair = input("Deseja [s]air ? ").lower().startswith('s') # deixando tudo minusculo e em caso comece com a letra "s"

    if sair is True:
        break 
