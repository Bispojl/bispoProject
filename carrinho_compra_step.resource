*** Settings ***
Resource    ../pages/carrinho_compra_page.resource
Resource    ../pages/cadastros_page.resource
Resource    ../pages/home_page.resource

*** Keywords ***

E realizo login utilizando credenciais de acesso
    Clicar no botao sign
    Preencher email de login
    Preencher senha de acesso
    Clicar no botao submit

Quando adiciono minha compra no carrinho
    Clicar no menu tshirts
    Clicar na primeira opcao de venda
    Sleep   20
    Clicar na opcao azul
    Clicar no botao adicionar ao carrinho
    Clicar no botao proceed
    Clicar no botao proceed checkout
    Sleep   5
    Preencher endereco adress
    Preencher endereco cidade
    Preencher endereco estado
    Preencher endereco cep
    Preencher endereco pais
    Preencher phone
    Preencher phone mobile
    Clicar no check box alias
    Clicar no botao save
    Clicar no botao proceed adress
    Clicar no check box terms
    Clicar no botao proceed shipping

E realizo o fluxo de pagamento
    Clicar na opcao de pagamento
    Clicar no botao confirma compra

Entao minha compra e realizada com sucesso
    Validar compra de produto
