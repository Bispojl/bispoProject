*** Settings ***
Resource    ../pages/cadastros_page.resource
Resource    ../pages/home_page.resource

*** Keywords ***
Quando realizo meu cadastro de novo usuario
    Dado que eu acesso o site de vendas
    Clicar no botao sign
    Preencher email de cadastro
    Clicar no botao criar conta
    Selecionar a opcao mr
    Preencher o campo first name
    Preencher o campo last name
    Preencher o campo de senha
    Selecionar a data de nascimento
    Selecionar o mes de nascimento
    Selecionar o ano de nascimento
    Selecionar SignUp
    Clicar no botao register
    Validar acesso a plataforma


Quando realizo meu cadastro com e-mail existente
    Dado que eu acesso o site de vendas
    Clicar no botao sign
    Preencher email de cadastro existente
    Clicar no botao criar conta


Entao meu cadastro e realizado com sucesso
    Validar acesso a plataforma
    Encerrar navegador


Entao a plataforma retorna erro de e-mail existente
    Validar e-mail existente
    Encerrar navegador