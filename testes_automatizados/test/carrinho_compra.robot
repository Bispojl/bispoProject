** Settings **
Library  SeleniumLibrary
Resource    ../steps/carrinho_compra_step.resource


** Test Cases **
Cenário 1: Efetuar a compra de um produto por uma das abas da plataforma web
    [Tags]    carrinho    minirregressivo
    Dado que eu acesso o site de vendas
    E realizo login utilizando credenciais de acesso
    Quando adiciono minha compra no carrinho
    E realizo o fluxo de pagamento
    Entao minha compra e realizada com sucesso
