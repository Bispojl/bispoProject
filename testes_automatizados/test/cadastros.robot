** Settings **
Library  SeleniumLibrary
Resource    ../steps/cadastros_step.resource


** Test Cases **
Cenário 1: Realizando cadastro de usuario
    [Tags]    cadastro    minirregressivo
    Dado que eu acesso o site de vendas
    Quando realizo meu cadastro de novo usuario
    Entao meu cadastro e realizado com sucesso

Cenário 2: Realizando cadastro de usuario
    [Tags]    cadastro    email_existente    minirregressivo
    Dado que eu acesso o site de vendas
    Quando realizo meu cadastro com e-mail existente
    Entao a plataforma retorna erro de e-mail existente