from behave import given, when, then

@given('estou na página de login')
def step_impl(context):
    context.browser.get(context.url + '/login')

@when('insiro um nome de usuário e senha válidos')
def step_impl(context):
    context.browser.find_element_by_name('nome').send_keys('usuario_valido')
    context.browser.find_element_by_name('senha').send_keys('senha_valida')
    context.browser.find_element_by_name('enviar').click()

@then('devo ser redirecionado para o painel')
def step_impl(context):
    assert context.browser.current_url == context.url + '/home'

@when('insiro um nome de usuário e senha inválidos')
def step_impl(context):
    context.browser.find_element_by_name('nome').send_keys('usuario_invalido')
    context.browser.find_element_by_name('senha').send_keys('senha_invalida')
    context.browser.find_element_by_name('enviar').click()

@then('devo ver uma mensagem de erro')
def step_impl(context):
    assert "Credenciais inválidas" in context.browser.page_source