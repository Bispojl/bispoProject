'''
NOT (nao) usado para inverter expressao
not True = False
not False = True
'''

print("========== SISTEMA ==========")
print()
login = input("digite [E]ntrar ou [S]air...")
senha = input("digite sua senha de acesso: ")
senha_credenciada = "bispo3"

if  login == 'S' or login == 's':
    print("voce saiu do sistema")
elif not senha:
    print("voce nao digitou uma senha")
elif senha != senha_credenciada:
    print("senha incorreta")
else:
    print("bem vindo")