from behave import given, when, then
from pages.practice_form_page import PracticeFormPage
import os

@given('que eu acesso a página de formulário de prática')
def step_impl(context):
    context.practice_form_page = PracticeFormPage(context.driver)
    context.practice_form_page.navigate()

@when('eu preencho todo o formulário com dados aleatórios')
def step_impl(context):
    context.practice_form_page.fill_form_with_random_data()

@when('eu faço o upload de um arquivo de texto')
def step_impl(context):
    file_path = os.path.join(context.resources_path, 'upload_file.txt')
    context.practice_form_page.upload_file(file_path)

@when('eu submeto o formulário')
def step_impl(context):
    context.practice_form_page.submit_form()

@when('um popup de confirmação deve ser exibido')
def step_impl(context):
    assert context.practice_form_page.is_modal_visible(), "O modal de confirmação não foi exibido."

@then('eu fecho o popup de confirmação')
def step_impl(context):
    context.practice_form_page.close_modal()