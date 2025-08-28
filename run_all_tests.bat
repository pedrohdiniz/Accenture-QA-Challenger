@echo off
echo ===================================================
echo EXECUTANDO: DESAFIO API - PARTE 1
echo ===================================================
python api_challenge.py

REM Verifica se o teste de API falhou
if %errorlevel% neq 0 (
    echo.
    echo Ocorreu um erro no Desafio de API. A execucao sera interrompida.
    exit /b %errorlevel%
)

echo.
echo ===================================================
echo EXECUTANDO: DESAFIO FRONTEND - PARTE 2
echo ===================================================
cd Frontend_Challenger
behave
cd ..

echo.
echo ===================================================
echo TODOS OS DESAFIOS FORAM EXECUTADOS.
echo ===================================================
pause