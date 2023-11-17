# Food Fact API Rest

## Food Fact - Objetivo
Desenvolver uma REST API que utilizará os dados da Open Food Facts um banco de dados aberto com informçaões nutricionais de vários produtos.

### Linguagens, Frameworks e Biblotecas usadas
- Python=3.11.12
- Django==4.2.6
- BeautfulSoup
- aiohttp==3.8.6
- beautifulsoup4==4.12.2
- OpenAPI (para documentar a API)

### Banco de dados
Foi usado o sqlite3 como banco de daods para armezar os dados.

### O Projeto
Este projeto consiste em um sistema de scraping que faz a raspagem de dados nutricionais de prodututos alimentares da página [Open Food Facts](https://world.openfoodfacts.org/), armezena as informações no banco de dados e disponibiliza essas informações no formato Json através do endpoints.

A API apresenta os seguintes dados de cada produto: [products.json](./products.json)

### Sincronização dos produtos
O scraping e sincrização dos produtos para o banco de dados acontecerá diariamente as 09:30.

### Tests
Todas as funões de test dos endpoints e do banco do banco de dados estão no arquivo tests.py na app do projeto (diretório food_fact).

### Rodar o programa
Para acessar a API:
- Acessar o serviço em (https://foodfact-production.up.railway.app/)
- Exibir as páginas de acordo com os endpoints

Os endpoints da API são:
- `GET /`: Retorna um Status: 200 e uma Mensagem "API Food Fact";
- `GET /products`: Lista todos os produtos da base de dados, separando por página, cada página terá 10 produtos;
- `GET /products/search`: Filtra produto através do nome ou produto;
- `GET /products/code`: Obtém a informação somente de um produto. Code é um número iteiro;

Foi utilizado o sistema de Paginação para exibir na interface da API, são exibidos 10 produtos por página. Para mudar outras páginas informa o seguinte caminho: http://127.0.0.1:8000/products/?page=numero_da_pagina

Número da página recebe um valor númerico inteiro.

Para mais informações e exemplos acessa a documentação do projeto:
[Food Fact](https://app.swaggerhub.com/apis/SabinoEduardo/food-fact_open_api_3_0/1.0.0)
