Feature: Login Functionality

  Scenario: Successful login with valid credentials
    Given estou na página de login
    When insiro um nome de usuário e senha válidos
    Then devo ser redirecionado para o painel

  Scenario: Unsuccessful login with invalid credentials
    Given estou na página de login
    When insiro um nome de usuário e senha inválidos
    Then devo ver uma mensagem de erro