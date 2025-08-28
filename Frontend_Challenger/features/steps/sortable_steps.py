from behave import given, when, then
from pages.sortable_page import SortablePage

@given(u'que eu acesso a página de itens ordenáveis')
def step_impl(context):
    context.sortable_page = SortablePage(context.driver)
    context.sortable_page.navigate()

@when(u'eu ordeno os itens da lista para a ordem crescente')
def step_impl(context):
    context.target_order = ["One", "Two", "Three", "Four", "Five", "Six"]
    context.sortable_page.sort_list_to_order(context.target_order)

@then(u'a lista deve estar na ordem "One", "Two", "Three", "Four", "Five", "Six"')
def step_impl(context):
    final_order = context.sortable_page.get_current_list_order()
    assert final_order == context.target_order, f"A ordem final está incorreta. Esperado: {context.target_order}, Obtido: {final_order}"