from behave import given, when, then
from pages.browser_windows_page import BrowserWindowsPage

@given('que eu acesso a página de janelas do navegador')
def step_impl(context):    
    context.browser_windows_page = BrowserWindowsPage(context.driver)
    context.browser_windows_page.navigate()

@when('eu clico no botão "New Window"')
def step_impl(context):
    context.browser_windows_page.click_new_window()

@then('uma nova janela deve ser aberta com a mensagem "{message}"')
def step_impl(context, message):
    context.browser_windows_page.switch_to_new_window()
    recived_message = context.browser_windows_page.get_new_window_message()
    expected_message = message
    assert recived_message == expected_message, f"ERRO: Mensagem esperada era '{expected_message}', mas a mensagem encontrada foi '{recived_message}'"

@then('eu fecho a nova janela e retorno para a original')
def step_impl(context):
    context.browser_windows_page.close_new_window_and_switch_back()