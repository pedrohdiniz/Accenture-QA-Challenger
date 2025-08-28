#!/bin/bash

echo "==================================================="
echo "EXECUTANDO: DESAFIO API - PARTE 1"
echo "==================================================="
python3 api_challenge.py

# Verifica se o teste de API falhou
API_EXIT_CODE=$?
if [ $API_EXIT_CODE -ne 0 ]; then
    echo ""
    echo "Ocorreu um erro no Desafio de API. A execução será interrompida."
    exit $API_EXIT_CODE
fi

echo ""
echo "==================================================="
echo "EXECUTANDO: DESAFIO FRONTEND - PARTE 2"
echo "==================================================="
cd Frontend_Challenger
behave
cd ..

echo ""
echo "==================================================="
echo "TODOS OS DESAFIOS FORAM EXECUTADOS."
echo "==================================================="