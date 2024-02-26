""" 
com o parametro >>sep<< podemos escolher a forma que iremos separar os argumentos
dentro dos parenteses
"""
print(30, 40, 50, sep=' ')
print(100, 200, 300, sep=" - ")

# Aspas simples, 
# o interpretador do python identificara um texto
print('Joao Bispo')

# Aspas duplas, 
# o interpretador do python identificara um texto
print("Joao Bispo")

# Escape, 
# utilizado para que voce igone um caractere dentro de um argumento
print("Joao \"Bispo\"") # agora o interpretador ira manter o nome Bispo entre aspas duplas

#r 
# utilizado para mostrar o caractere do escape
print(r"Joao \"Bispo\"")

# A FORMA CORRETA CASO QUEIRA MOSTRAR ASPAS DENTRO DE UMA TEXTO , -> USE OS DOIS TIPOS DE ASPAS, DESDE QUE INICIEI E ENCERRE
#COM O MESMO TIPO
print("'JOAO BISPO'")
print('"JOAO BISPO"')