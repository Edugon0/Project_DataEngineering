# Project_DataEngineering

# Sistema de Análise de Vendas para Concessionária de Carros

Este projeto é um sistema de engenharia de dados criado para uma empresa fictícia de uma concessionária de carros. O sistema fornecia análises detalhadas de vendas por concessionária Chamada NovaDrivers um projeto montado dentro de um bootcamp de engenheiro de dados, vendas por veículo, vendas por vendedor e uma análise temporal das vendas.

## Descrição

O objetivo deste projeto foi demonstrar a criação de um pipeline de dados completo, desde a extração dos dados até a análise final, utilizando diversas ferramentas e tecnologias de engenharia de dados.

**Nota:** Devido aos custos associados às ferramentas pagas (Snowflake e AWS), o sistema completo foi removido. No entanto, a documentação a seguir descreve as funcionalidades e as tecnologias utilizadas.

## Tecnologias Utilizadas

- **PostgreSQL:** Banco de dados relacional utilizado para armazenar dados brutos.
- **AWS EC2:** Instâncias de computação na nuvem usadas para hospedar o Airflow e o PostgreSQL.
- **Linux (Ubuntu):** Sistema operacional utilizado nas instâncias EC2.
- **Apache Airflow:** Ferramenta de orquestração de fluxo de trabalho utilizada para gerenciar e automatizar o pipeline de dados, configurada dentro da instância EC2.
- **Docker:** Instalado dentro da instância Linux EC2 para gerenciamento de contêineres.
- **Snowflake:** Data warehouse utilizado para armazenar e analisar grandes volumes de dados.
- **DBT (Data Build Tool):** Ferramenta de transformação de dados que permite transformar dados no Snowflake.
- **Google Looker:** Ferramenta de BI utilizada para criar dashboards interativos.

## Método de LT (Load Transform)

Utilizamos o método de LT (Load Transform) para carregar os dados brutos diretamente no data warehouse (Snowflake) e, em seguida, realizar as transformações necessárias utilizando DBT. Esse método nos permite manter a integridade dos dados brutos enquanto aplicamos transformações para análise e relatórios.

## Estrutura do Projeto

```plaintext
├── data
│   ├── raw_data.sql
│   ├── transformed_data.sql
├── airflow
│   ├── dags
│   │   ├── etl_pipeline.py
├── dbt
│   ├── models
│   │   ├── staging
│   │   │   ├── staging_sales.sql
│   │   ├── marts
│   │   │   ├── sales_analysis.sql
├── sql_scripts
│   ├── sales_by_dealership.sql
│   ├── sales_by_vehicle.sql
│   ├── sales_by_seller.sql
│   ├── temporal_analysis.sql
├── README.md
└── requirements.txt
