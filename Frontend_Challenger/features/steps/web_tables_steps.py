from behave import given, when, then
from pages.web_tables_page import WebTablesPage

@given('que eu acesso a página de tabelas web')
def step_impl(context):
    context.web_tables_page = WebTablesPage(context.driver)
    context.web_tables_page.navigate()

# --- Steps do Scenario 1 ---
@when('eu adiciono um novo registro com dados aleatórios')
def step_impl(context):
    context.user_data = context.web_tables_page.add_new_record()
    assert context.web_tables_page.is_record_present(context.user_data['email']), "O registro não foi adicionado à tabela."

@when('eu edito o registro recém-criado com novos dados aleatórios')
def step_impl(context):
    context.new_user_data = context.web_tables_page.edit_record(context.user_data['email'])
    assert context.web_tables_page.is_record_present(context.new_user_data['email']), "O registro não foi editado corretamente."

@then('eu deleto o registro editado e valido sua remoção')
def step_impl(context):
    context.web_tables_page.delete_record(context.new_user_data['email'])
    assert not context.web_tables_page.is_record_present(context.new_user_data['email']), "O registro não foi deletado da tabela."

# --- Steps do Scenario 2 (@bonus) ---
@when('eu crio {count:d} novos registros de forma dinâmica')
def step_impl(context, count):
    context.initial_rows = context.web_tables_page.get_row_count()
    context.web_tables_page.add_multiple_records(count)
    
@then('eu deleto todos os {count:d} registros criados')
def step_impl(context, count):
    context.web_tables_page.delete_all_added_records(context.initial_rows)
    assert context.web_tables_page.get_row_count() == context.initial_rows, "Todos os registros não foram deletados."