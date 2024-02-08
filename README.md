# Projeto de exemplo de automação com Robot

- [O que é o Robot Framework](#o-que-é-o-robot-framework)
- [Conheça mais sobre Robot Framework](#conheça-mais-sobre-robot-framework)
- [Conheça mais sobre Selenium](#conheça-mais-sobre-o-selenium)
- [Início rápido](#Início-rápido)


Esse é um exemplo de projeto de automação de testes mobile com _Robot Framework_, mantido pela squad [Quality Platform](https://iconectados.sharepoint.com/sites/itihub/SitePages/sqd-qualidade.aspx).

## O que é o Robot Framework

O _Robot Framework_ é um _framework_ de automação de testes de código aberto usado para testar aplicativos de software. Ele fornece uma estrutura de teste genérica que é fácil de usar e implementar, mesmo para usuários com pouca experiência em programação.

Ele é baseado em linguagem de domínio específico (DSL), com sintaxe simples e legível, que permite aos usuários escreverem testes de forma clara e concisa. Ele suporta várias plataformas e tecnologias, incluindo aplicativos web, desktop, mobile, APIs e bancos de dados.

Além disso, ele é altamente extensível, permitindo que os usuários criem suas próprias bibliotecas e extensões personalizadas. Ele também suporta vários formatos de saída para relatórios de teste e integração com outras ferramentas de teste e gerenciamento de projetos.

## Conheça mais sobre Robot Framework

É importante ter compreensão de como usar o _Robot Framework_, assim como outras bibliotecas e ferramentas que orbitam seu uso.

Para facilitar essa jornada, seguem alguns recursos referenciais:

- [Guia do usuário do Robot Framework](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Documentação da API do Robot Framework](https://robot-framework.readthedocs.io/en/latest/)
- [Keywords nativas do Robot Framework](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html)
- [Keywords da biblioteca AppiumLibrary](http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html)
- [Keywords da biblioteca padrão Collections](https://robotframework.org/robotframework/latest/libraries/Collections.html)
- [Keywords da biblioteca padrão DateTime](https://robotframework.org/robotframework/latest/libraries/DateTime.html)
- [Keywords da biblioteca padrão Dialogs](https://robotframework.org/robotframework/latest/libraries/Dialogs.html)
- [Keywords da biblioteca padrão OperationsSystem](https://robotframework.org/robotframework/latest/libraries/OperatingSystem.html)
- [Keywords da biblioteca padrão Process](https://robotframework.org/robotframework/latest/libraries/Process.html)
- [Documentação do analisador estático de código Robocop](https://robocop.readthedocs.io/en/stable/)
- [Documentação do gerenciador de teste tox](https://tox.wiki/en/latest/)
- [Documentação formatador EditorConfig](https://editorconfig.org/)

## Conheça mais sobre o selenium
- [Documentação Selenium](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)


## Início rápido

Uma visão extremamente simplicada para executar esse projeto, sem se aprofundar em como os componentes funcionam e quais variáveis são obrigatórias, é a seguinte:

- Instale o module python.
- Instale o robotframework com o comando `pip3 install robotframework`.
- Instale a biblioteca do selenium com o comando `pip3 install robotframework-seleniumlibrary`.

- Inicie a automação passando o arquivo de execucao com `robot -d tests/cadastro.robot .` ou utilizando 

 
