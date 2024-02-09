*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${input_login_email}         id:email
${input_login_passw}         id:passwd
${btn_login_submit}          id:SubmitLogin
${btn_t_shirts}              xpath:/html/body/div[1]/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a
${btn_01_tshirts}            xpath:/html/body/div[1]/div[2]/div/div[3]/div[2]/ul/li/div/div[1]/div/a[1]/img
${btn_color_orange}          id:color_13
${btn_color_blue}            id:color_14
${btn_add_to_car}            id:add_to_cart
${btn_proceed}               xpath:/html/body/div[1]/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/div[4]/a/span
${btn_proceed_checkout}      xpath:/html/body/div[1]/div[2]/div/div[3]/div/p[2]/a[1]/span
${input_adress}              id:address1
${input_city}                id:city
${input_state}               id:id_state
${input_post_code}           id:postcode
${input_country}             id:id_country
${input_phone}               name:phone
${input_mobile}              id:phone_mobile
${input_alias}               name:alias
${btn_save}                  xpath:/html/body/div[1]/div[2]/div/div[3]/div/div/form/p[2]/button/span
${btn_proceed_adress}        xpath:/html/body/div[1]/div[2]/div/div[3]/div/form/p/button/span
${box_terms}                 id:cgv
${btn_proceed_shipping}      xpath:/html/body/div[1]/div[2]/div/div[3]/div/div/form/p/button/span
${btn_pay_by_bank}           xpath:/html/body/div[1]/div[2]/div/div[3]/div/div/div[3]/div[1]/div/p/a
${btn_confirm}               xpath:/html/body/div[1]/div[2]/div/div[3]/div/form/p/button/span
${label_sucess_pay}          class:alert-success

*** Keywords ***

Preencher email de login
    Wait Until Element Is Visible    ${input_login_email} 
    Input Text    ${input_login_email}     jlbispojr@gmail.com.br

Preencher senha de acesso
    Wait Until Element Is Visible    ${input_login_passw} 
    Input Text    ${input_login_passw}     jlbispojr0912

Clicar no botao submit
    Wait Until Element Is Visible    ${btn_login_submit} 
    Click Element    ${btn_login_submit}

Clicar no menu tshirts
    Wait Until Element Is Visible    ${btn_t_shirts}  
    Click Element    ${btn_t_shirts}  

Clicar na primeira opcao de venda
    Wait Until Element Is Visible    ${btn_01_tshirts}  
    Click Element    ${btn_01_tshirts} 

Clicar na opcao azul
    Wait Until Element Is Visible     ${btn_color_blue}
    Click Element    ${btn_color_blue}

Clicar no botao adicionar ao carrinho
    Wait Until Element Is Visible    ${btn_add_to_car}  
    Click Element    ${btn_add_to_car} 

Clicar no botao proceed
    Wait Until Element Is Visible    ${btn_proceed} 
    Click Element    ${btn_proceed}

Clicar no botao proceed checkout
    Wait Until Element Is Visible    ${btn_proceed_checkout} 
    Click Element    ${btn_proceed_checkout}

Preencher endereco adress
    Wait Until Element Is Visible    ${input_adress}  
    Input Text    ${input_adress}     luis carlos de assumpcao

Preencher endereco cidade
    Wait Until Element Is Visible    ${input_city}  
    Input Text    ${input_city}     Sao Paulo

Preencher endereco estado
    Select From List By Value    ${input_state}    1

Preencher endereco cep
    Wait Until Element Is Visible    ${input_post_code} 
    Input Text    ${input_post_code}     10004

Preencher endereco pais
    Select From List By Value    ${input_state}    21
    
Preencher phone
    Wait Until Element Is Visible    ${input_phone} 
    Input Text    ${input_phone}     1139170408

Preencher phone mobile
    Wait Until Element Is Visible    ${input_mobile} 
    Input Text    ${input_mobile}      11962072484

Clicar no check box alias
    Wait Until Element Is Visible    ${input_alias} 
    Click Element    ${input_alias} 

Clicar no botao save
    Wait Until Element Is Visible    ${btn_save} 
    Click Element    ${btn_save}

Clicar no botao proceed adress
    Wait Until Element Is Visible   {btn_proceed_adress}
    Click Element    {btn_proceed_adress}

Clicar no check box terms
    Wait Until Element Is Visible    ${box_terms} 
    Click Element    ${box_terms} 

Clicar no botao proceed shipping
    Wait Until Element Is Visible    ${btn_proceed_shipping}
    Click Element    ${btn_proceed_shipping}

Clicar na opcao de pagamento
    Wait Until Element Is Visible    ${btn_pay_by_bank}  
    Click Element    ${btn_pay_by_bank} 

Clicar no botao confirma compra
    Wait Until Element Is Visible    ${btn_confirm}   
    Click Element    ${btn_confirm}  

Validar compra de produto
    Wait Until Element Is Visible    ${label_sucess_pay}
