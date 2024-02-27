''' 
Operadores logicos
and (e) or (ou) not (nao)
and - Todas as condicoes precisam ser verdadeira. Se qualquer valor for considerado falso
a expressao inteira sera avaliada naquele valor.
'''    
print("========== SISTEMA ==========")
print("")
login = input("Digite seu usuario: ")
senha = input("digite sua senha: ")
senha_de_acesso = "bispo3"

if(login == "jlbispo" and senha == senha_de_acesso):
    print("login realizado com sucesso")
else:
    print(f'login "{login}" ou senha "{senha}", estao incorretos !')

''' 
OR (ou) - Qualquer condicao verdadeira avalia toda expresssa em verdadeira 
'''
print("========== SISTEMA ==========")
print()
login = input("digite [E]ntrar ou [S]air...")
senha = input("digite sua senha de acesso: ")
senha_credenciada = "bispo3"

if(login == "E" or login == "e") and senha == senha_credenciada:
    print("login realizado com sucesso")
elif login == "S" or login == "s":
    print("voce solicitou logout")
elif senha == "":
    print("voce nao digitou a senha")
else:
    print("Login ou senha incorretos, voce saiu do sistema")