from behave import given, when, then
from pages.progress_bar_page import ProgressBarPage

@given(u'que eu acesso a página da barra de progresso')
def step_impl(context):
    context.progress_bar_page = ProgressBarPage(context.driver)
    context.progress_bar_page.navigate()

@when(u'eu clico no botão "Start"')
def step_impl(context):
    context.progress_bar_page.click_start_stop_button()

@when(u'eu paro a barra de progresso antes de 25%')
def step_impl(context):
    context.progress_bar_page.wait_for_progress_to_be_greater_than(10)
    context.progress_bar_page.click_start_stop_button()

@when(u'eu valido que o valor da barra é menor ou igual a 25%')
def step_impl(context):
    value = context.progress_bar_page.get_progress_value()
    assert value <= 25, f"O valor da barra é {value}, que é maior que 25."

@when(u'eu clico em "Start" novamente')
def step_impl(context):
    context.progress_bar_page.click_start_stop_button()

@when(u'aguardo a barra de progresso chegar a 100%')
def step_impl(context):
    context.progress_bar_page.wait_for_progress_to_reach(100)

@then(u'o botão deve mudar para "Reset" e eu clico nele para zerar a barra')
def step_impl(context):
    context.progress_bar_page.click_reset_button_when_visible()
    valor_atual = context.progress_bar_page.get_progress_value()
    assert valor_atual == 0, f"Falha na verificação! A barra deveria estar em 0, mas estava em {valor_atual}."