# Desafio de engenharia de dados da Refera


O objetivo desse desafio é ser algo rápido para exemplificar alguns desafios do dia a dia de quem trabalha com dados. Queremos com esse desafio avaliar o seu conhecimento básico em programação, banco de dados e entender mais quais as boas práticas você segue para construção de código.


## O desafio

Com o objetivo de evitar a sobrecarga no banco de dados `Transactional`, é necessária a criação de um novo ambiente para a execução das análises. Portanto, foi criado um segundo banco de dados (`Analytics`) com uma cópia das tabelas do banco de origem.

O arquivo [docker-compose.yml](docker-compose.yml) ativa containers com os bancos de dados `transactional` e `analytics` e também com `python`, para rodar o script de extração e carga.

![Infra dos banco de dados](fluxo.png)

## Configuração do Ambiente

Docker Version: 20.10.23