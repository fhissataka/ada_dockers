# Projeto Final do módulo de containers, do curso de DevOps do ADA-iFood
# por Fernando Hissataka, janeiro de 2024

Este é um projeto simples Dockerizado usando FastAPI (Python) e MySQL. 

O projeto inclui a configuração de Docker Compose para executar um container FastAPI conectado a um banco de dados MySQL.

## Configuração

Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

## Executando o Projeto

Para iniciar o projeto, execute o seguinte comando na raiz do projeto:

docker-compose up -d

## Testando o Projeto

Abra um browser, e acesse a porta 80: 

http://localhost:80

Clique nos links fornecidos para acessar as funções programadas no Python de acesso ao banco de dados


## Rotas Disponíveis

## Raiz

URL: http://localhost
Descrição: Página Principal


## Inicializar Banco de Dados:

URL: http://localhost/inicia
Descrição: Inicializa o banco de dados.


## Inserir Dados de Amostra:

URL: http://localhost/insere
Descrição: Insere dados de amostra na tabela do banco de dados.

## Deletar dados:

URL: http://localhost/deleta
Descrição: Deleta todos os dados da tabela do banco de dados.


## Consultar Dados:

URL: http://localhost/pesquisa
Descrição: Recupera e exibe os dados da tabela do banco de dados.

