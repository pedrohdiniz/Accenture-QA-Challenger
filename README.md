# Accenture QA Challenger

Este repositório contém a solução completa para o desafio técnico de automação de testes, dividido em duas partes:
1.  **API Testing**: Um script Python que testa um fluxo de criação e gerenciamento de usuário e livros.
2.  **Frontend Testing**: Uma suíte de testes de interface web utilizando Python, Selenium e BDD (Behave), simulando a interação real de um usuário com o site [demoqa.com](https://demoqa.com/).

## Tecnologias Utilizadas

* **Linguagem**: Python
* **Testes de API**: `requests`
* **Testes de Frontend**:
    * `selenium`: Para automação do navegador.
    * `behave`: Framework BDD (equivalente ao Cucumber para Python).
    * `webdriver-manager` ou **Driver Manual**: Para gerenciar o driver do Chrome.
* **Padrões de Projeto**: Page Object Model (POM) para organizar o código de frontend.

---

## Passo a Passo para Execução

Siga estas instruções para configurar o ambiente e rodar os testes.

### 1. Pré-requisitos

* **Python 3.8+**: [Baixe aqui](https://www.python.org/downloads/). (Durante a instalação no Windows, marque a opção "Add Python to PATH").
* **Google Chrome**: Navegador web atualizado.
* **Git**: [Baixe aqui](https://git-scm.com/downloads/).

### 2. Configuração do Ambiente

**a. Clone o Repositório**
Abra um terminal (CMD, PowerShell, ou Terminal) e clone este projeto para a sua máquina:
git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
cd ACCENTURE_QA_CHALLENGER

**b. Crie e Ative um Ambiente Virtual**
Comando para criar a pasta do ambiente virtual (só precisa ser feito uma vez)
python -m venv venv

Comando para ATIVAR o ambiente (precisa ser feito toda vez que abrir um novo terminal)
# Windows:
.\venv\Scripts\activate

# macOS ou Linux:
source venv/bin/activate

**c. Dependências**
pip install -r requirements.txt

**d. Configurando o Chromedriver.exe**
Este projeto está configurado para usar um driver manual para maior controle.

Verifique a sua versão do Google Chrome: Vá em Menu (...) > Ajuda > Sobre o Google Chrome. Anote a versão (ex: 128.0.6613.84).

Baixe o driver correspondente: Acesse a página Chrome for Testing Downloads, encontre a sua versão na seção Stable e baixe o chromedriver correspondente com o seu sistema operacional.

Adicione ao projeto: Descompacte o arquivo e coloque o chromedriver.exe na pasta raiz deste projeto (na mesma pasta do arquivo README.md).

### 3. Executando os Testes
Com o ambiente configurado e o ambiente virtual (venv) ativo, você pode executar os testes. 

**Windows**
Na pasta raiz do projeto, execute o script principal
.\run_all_tests.bat

**macOS ou Linux**
sh run_all_tests.sh