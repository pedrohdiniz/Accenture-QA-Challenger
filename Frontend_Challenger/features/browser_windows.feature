Feature: Manipulação de Janelas do Navegador
  Como um usuário, eu quero interagir com novas janelas abertas pela aplicação
  para garantir que o sistema consegue lidar com múltiplos contextos de navegador.

  Scenario: Scenario name: Validar a abertura e o conteúdo de uma nova janela
    Given que eu acesso a página de janelas do navegador
    When eu clico no botão "New Window"
    Then uma nova janela deve ser aberta com a mensagem "This is a sample page"
    Then eu fecho a nova janela e retorno para a original