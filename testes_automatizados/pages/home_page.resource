*** Settings ***
Library    SeleniumLibrary
*** Variables ***

${url}                 http://www.automationpractice.pl/index.php/
${browser}             chrome

*** Keywords ***

Dado Que eu acesso o Site de vendas
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

Encerrar Navegador
    Close Browser