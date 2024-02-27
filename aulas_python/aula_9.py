# IF / ELIF ...../ ELSE
# SE / SE NAO SE / SE NAO

login = input("Digite a senha para acessar:")
numero_inteiro = (int(login))

if numero_inteiro == 123:
    print("login realizado com sucesso")
elif numero_inteiro == 0:
    print("codigo mestre acessado...aguarde o reset de senha")
else:
    print("acesso negado, senha incorreta.")