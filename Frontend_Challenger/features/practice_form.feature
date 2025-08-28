Feature: Preenchimento de Formulário de Prática
  Como um usuário, eu quero preencher e submeter o formulário de registro
  para garantir que os dados sejam enviados corretamente.

  Scenario: Preenchimento e envio bem-sucedido do formulário de estudante
    Given que eu acesso a página de formulário de prática
    When eu preencho todo o formulário com dados aleatórios
    And eu faço o upload de um arquivo de texto
    And eu submeto o formulário
    And um popup de confirmação deve ser exibido
    Then eu fecho o popup de confirmação