Feature: Ordenação de Itens
  Como um usuário, eu quero reordenar itens em uma lista
  usando a funcionalidade de arrastar e soltar (drag and drop).

  Scenario: Ordenar a lista de forma crescente
    Given que eu acesso a página de itens ordenáveis
    When eu ordeno os itens da lista para a ordem crescente
    Then a lista deve estar na ordem "One", "Two", "Three", "Four", "Five", "Six"