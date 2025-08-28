from datetime import datetime
import requests
import json
import random
import string

# URL base da API
base_url = "https://demoqa.com"

# --- Funções Auxiliares ---
def formatted_timestamp():
  """
  Gera uma string com o timestamp no formato AAAAMMDDhhmmss.
  """
 
  return datetime.now().strftime('%Y%m%d%H%M%S')

def print_response(name, response):
    """Imprime o nome da requisição, o status code e a resposta em JSON."""
    print(f"--- {name} ---")
    print(f"Status Code: {response.status_code}")
    try:
        # Tenta imprimir a resposta como JSON formatado
        print(f"Response Body: {json.dumps(response.json(), indent=2)}")
    except json.JSONDecodeError:
        # Se não for JSON, imprime como texto
        print(f"Response Body: {response.text}")
    print("-" * (len(name) + 8) + "\n")

# --- Execução do Desafio ---

def run_api_challenge():
    # Dados do novo usuário (aleatórios para garantir que o script possa ser executado várias vezes)
    timestamp = formatted_timestamp()
    username = f"qa_desafio_{timestamp}"
    password = f"Senha@{timestamp.capitalize()}123!"
    user_id = None
    token = None

    # Headers padrão
    headers = {
        "Content-Type": "application/json"
    }

    print("="*50)
    print(">>> INICIANDO DESAFIO DE API <<<")
    print("="*50 + "\n")

    # Passo 1: Criar um usuário
    print(">>> Passo 1: Criar Usuário <<<")
    create_user_payload = {
        "userName": username,
        "password": password
    }
    create_user_response = requests.post(
        f"{base_url}/Account/v1/User",
        headers=headers,
        data=json.dumps(create_user_payload)
    )
    print_response("Criação de Usuário", create_user_response)

    if create_user_response.status_code == 201:
        user_id = create_user_response.json().get("userID")
        print(f"Sucesso! Usuário criado com UserID: {user_id}\n")
    else:
        print("Falha ao criar usuário. Encerrando o script de API.")
        return False

    # Passo 2: Gerar um token de acesso
    print(">>> Passo 2: Gerar Token de Acesso <<<")
    generate_token_payload = {
        "userName": username,
        "password": password
    }
    generate_token_response = requests.post(
        f"{base_url}/Account/v1/GenerateToken",
        headers=headers,
        data=json.dumps(generate_token_payload)
    )
    print_response("Geração de Token", generate_token_response)

    if generate_token_response.status_code == 200:
        token = generate_token_response.json().get("token")
        print("Sucesso! Token gerado.\n")
    else:
        print("Falha ao gerar token. Encerrando o script de API.")
        return False

    # Adiciona o token ao header para as próximas requisições autenticadas
    auth_headers = headers.copy()
    auth_headers["Authorization"] = f"Bearer {token}"

    # Passo 3: Confirmar se o usuário criado está autorizado
    print(">>> Passo 3: Validar Autorização do Usuário <<<")
    # Reutilizando o payload de geração de token
    authorized_response = requests.post(
        f"{base_url}/Account/v1/Authorized",
        headers=auth_headers,
        data=json.dumps(generate_token_payload)
    )
    print_response("Validação de Autorização", authorized_response)

    if authorized_response.status_code != 200 or not authorized_response.json():
        print("Usuário não autorizado. Encerrando o script de API.")
        return False
    else:
        print("Sucesso! Usuário está autorizado.\n")


    # Passo 4: Listar os livros disponíveis
    print(">>> Passo 4: Listar Livros Disponíveis <<<")
    list_books_response = requests.get(f"{base_url}/BookStore/v1/Books", headers=auth_headers)
    print_response("Listagem de Livros (Status)", list_books_response)


    if list_books_response.status_code != 200:
        print("Falha ao listar livros. Encerrando o script de API.")
        return False

    all_books = list_books_response.json().get("books", [])
    if len(all_books) < 2:
        print("Não há livros suficientes para alugar. Encerrando o script de API.")
        return False
    else:
        print(f"Sucesso! {len(all_books)} livros encontrados.\n")


    # Passo 5: Alugar dois livros de livre escolha
    print(">>> Passo 5: Alugar Dois Livros <<<")
    # Seleciona os dois primeiros livros da lista
    books_to_add = [all_books[0], all_books[1]]
    isbn1 = books_to_add[0]['isbn']
    isbn2 = books_to_add[1]['isbn']
    print(f"Livros selecionados para aluguel (ISBN): {isbn1} e {isbn2}")

    add_books_payload = {
        "userId": user_id,
        "collectionOfIsbns": [
            {"isbn": isbn1},
            {"isbn": isbn2}
        ]
    }
    add_books_response = requests.post(
        f"{base_url}/BookStore/v1/Books",
        headers=auth_headers,
        data=json.dumps(add_books_payload)
    )
    print_response("Adicionar Livros à Coleção", add_books_response)

    if add_books_response.status_code != 201:
        print("Falha ao alugar os livros. Encerrando o script de API.")
        return False
    else:
        print("Sucesso! Livros alugados.\n")

    # Passo 6: Listar os detalhes do usuário com os livros escolhidos
    print(">>> Passo 6: Listar Detalhes do Usuário com Livros <<<")
    get_user_response = requests.get(
        f"{base_url}/Account/v1/User/{user_id}",
        headers=auth_headers
    )
    print_response("Detalhes do Usuário com Livros", get_user_response)

    if get_user_response.status_code == 200:
        user_books = get_user_response.json().get("books", [])
        if len(user_books) == 2:
            print("\n>>> DESAFIO API CONCLUÍDO COM SUCESSO! <<<")
            return True
        else:
            print("\n>>> FALHA NA VALIDAÇÃO FINAL DO DESAFIO API. O número de livros alugados está incorreto. <<<")
            return False
    else:
        print("\n>>> FALHA AO CONCLUIR O DESAFIO API. Não foi possível obter os detalhes do usuário. <<<")
        return False

if __name__ == "__main__":
    run_api_challenge()