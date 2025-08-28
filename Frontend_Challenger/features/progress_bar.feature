Feature: Interação com a Barra de Progresso
  Como um usuário, eu quero iniciar, parar e resetar uma barra de progresso
  para validar seu comportamento dinâmico.

  Scenario: Controlar a barra de progresso
    Given que eu acesso a página da barra de progresso
    When eu clico no botão "Start"
    And eu paro a barra de progresso antes de 25%
    And eu valido que o valor da barra é menor ou igual a 25%
    And eu clico em "Start" novamente
    And aguardo a barra de progresso chegar a 100%
    Then o botão deve mudar para "Reset" e eu clico nele para zerar a barra