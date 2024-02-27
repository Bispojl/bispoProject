#introducao a f-string, -> podemos formatar uma string para que o codigo fique mais natural
nome = "João Bispo"
altura = 1.75
peso = 95
imc = peso / (altura ** 2)
imc2 = peso / (altura * altura)

linha_1 = f"{nome} tem {altura} de altura,"
linha_2 = f"pesa {peso} quilos e seu imc é {imc2:.2f}" #setando que quero apenas duas casas decimais depois do "."

print(linha_1)
print(linha_2)
print()
print()

#utilizando o metodo format, funcao dentro do objeto "string"
texto = '{} tem {} de altura e pesa {} quilos, seu imc é de : {:.2f}'
text_formatado = texto.format(nome, altura, peso, imc)
print(text_formatado)
print()
print()


#modelo 1 utilizando o .format
nome = input("qual o seu nome ? ")
resultado = 'jogador 1, seu nome é {}'
resultado_formatado = resultado.format(nome)
print(resultado_formatado)
print()
print()

#modelo 2 utilizando o f' string 
nome = input("qual o seu nome ? ")
print(f'jogador 2, seu nome é  {nome}')