# Ferramenta de backup com distribuição em multiprocessos
Uma ferramenta de backups distribuida, usando threads e multiprocessos.

Um trabalho de:
`Ana Flávia`, `João Vítor Bortoluz` e `Marina Barbosa`

## Requirements
`Python` e um compilador de `C++`

## Setup
- Alterar o ip do `HOST` em `client/backup_tool.py`

- Compilar o código `C++` `server/backup_exec.cpp` na máquina servidor:
`g++ -std=c++17 backup_exec.cpp -o backup_exec`

## Como executar
Para mandar um arquivo para o servidor:
`python backup_tool.py send example.txt`

Para alterar o local padrão onde serão salvos os arquivos no server edite o
`server/backup_exec.cpp` 
