@echo off
echo Iniciando o site BelasConfArte...
echo.

cd /d "%~dp0"

REM Verifica se o Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: Python não encontrado. Instale o Python e tente novamente.
    pause
    exit /b
)

REM Verifica se o app.py existe
if not exist "app.py" (
    echo ERRO: Arquivo app.py não encontrado!
    echo Verifique se este atalho está na pasta correta.
    pause
    exit /b
)

REM Abre o site no navegador
start "" "http://127.0.0.1:5000"

REM Inicia o servidor Flask
echo.
echo Servidor Flask iniciando...
echo Acesse o site no navegador.
echo Para parar o site, feche esta janela ou pressione Ctrl + C.
echo.
python app.py

pause