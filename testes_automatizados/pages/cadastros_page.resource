*** Settings ***
Library    SeleniumLibrary
*** Variables ***

${btn_sign}            class:login
${input_email}         id:email_create
${btn_sub}             id:SubmitCreate
${radio_title}         id:id_gender1
${input_firts_name}    id:customer_firstname
${input_last_name}     id:customer_lastname
${input_password}      id:passwd
${select_day}          id:days
${select_month}        id:months
${select_year}         id:years
${box_letter}          id:newsletter
${btn_register}        id:submitAccount
${label_sucess}        class:info-account
${falha_email}         id:create_account_error

*** Keywords ***

Clicar no botao sign
    Wait Until Element Is Visible    ${btn_sign}
    Click Element    ${btn_sign}

Preencher email de cadastro
    Wait Until Element Is Visible    ${input_email} 
    Input Text    ${input_email}     jlbispo@hotmail.com

Preencher email de cadastro existente
    Wait Until Element Is Visible    ${input_email} 
    Input Text    ${input_email}     jlbispojr@gmail.com

Clicar no botao criar conta
    Wait Until Element Is Visible    ${btn_sub}
    Click Element    ${btn_sub}

Selecionar a opcao mr
    Wait Until Element Is Visible    ${radio_title}
    Click Element    ${radio_title}
    
Preencher o campo first name
    Wait Until Element Is Visible    ${input_firts_name}
    Input Text    ${input_firts_name}    Joao
   
Preencher o campo last name
    Wait Until Element Is Visible    ${input_last_name}
    Input Text   ${input_last_name}    Bispo
     
Preencher o campo de senha
    Wait Until Element Is Visible    ${input_password}
    Input Text    ${input_password}    102030
    
Selecionar a data de nascimento
    Select From List By Value    ${select_day}   1

Selecionar o mes de nascimento
    Select From List By Value    ${select_month}   5

Selecionar o ano de nascimento
    Select From List By Value    ${select_year}   1996

Selecionar SignUp
    Click Element    ${box_letter}

Clicar no botao register
    Click Element    ${btn_register}


Validar acesso a plataforma
    Sleep   5
    Wait Until Element Is Visible   ${label_sucess}

Validar e-mail existente
    Wait Until Element Is Visible    ${falha_email}