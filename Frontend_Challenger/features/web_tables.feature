Feature: Interação com Tabelas Web
  Como um usuário, eu quero adicionar, editar e remover registros de uma tabela
  para garantir que as operações de CRUD funcionam corretamente.

  Scenario: Adicionar, editar e deletar um registro
    Given que eu acesso a página de tabelas web
    When eu adiciono um novo registro com dados aleatórios
    And eu edito o registro recém-criado com novos dados aleatórios
    Then eu deleto o registro editado e valido sua remoção

  @bonus
  Scenario: Adicionar e deletar múltiplos registros dinamicamente
    Given que eu acesso a página de tabelas web
    When eu crio 12 novos registros de forma dinâmica
    Then eu deleto todos os 12 registros criados