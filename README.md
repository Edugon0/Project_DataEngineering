# Projeto para Engenheira de dados

# Sistema de Análise de Vendas para Concessionária de Carros

Este projeto é um sistema de engenharia de dados criado para uma empresa fictícia de uma concessionária de carros. O sistema fornecia análises detalhadas de vendas por concessionária Chamada NovaDrivers um projeto montado dentro de um bootcamp de engenheiro de dados, vendas por veículo, vendas por vendedor e uma análise temporal das vendas.



  
## Descrição

O objetivo deste projeto foi demonstrar a criação de um pipeline de dados completo, desde a extração dos dados até a análise final, utilizando diversas ferramentas e tecnologias de engenharia de dados.

**Nota:** Devido aos custos associados às ferramentas pagas (Snowflake e AWS), o sistema completo foi removido. No entanto, a documentação a seguir descreve as funcionalidades e as tecnologias utilizadas.

## Funcionalidades
- Vendas por Concessionária: Análise das vendas segmentadas por cada concessionária.
- Vendas por Veículo: Análise das vendas segmentadas por cada modelo de veículo.
- Vendas por Vendedor: Análise das vendas realizadas por cada vendedor.
- Análise Temporal: Análise das vendas ao longo do tempo, permitindo identificar tendências sazonais e padrões de vendas.

## Tecnologias Utilizadas

- **PostgreSQL:** Banco de dados relacional utilizado para armazenar dados brutos.
- **AWS EC2:** Instâncias de computação na nuvem usadas para hospedar o Airflow e o PostgreSQL.
- **Linux (Ubuntu):** Sistema operacional utilizado nas instâncias EC2.
- **Apache Airflow:** Ferramenta de orquestração de fluxo de trabalho utilizada para gerenciar e automatizar o pipeline de dados, configurada dentro da instância EC2.
- **Docker:** Instalado dentro da instância Linux EC2 para gerenciamento de contêineres.
- **Snowflake:** Data warehouse utilizado para armazenar e analisar grandes volumes de dados.
- **DBT (Data Build Tool):** Ferramenta de transformação de dados que permite transformar dados no Snowflake.
- **Google Looker:** Ferramenta de BI utilizada para criar dashboards interativos.

## Dashboard no Google Looker
Os dados transformados seriam visualizados e analisados através de um dashboard interativo no Google Looker. Este dashboard permitiria:

 Visualizar métricas de vendas em tempo real.
 Filtrar e segmentar dados de vendas por diferentes dimensões, como concessionária, veículo, e vendedor.
 Analisar tendências de vendas ao longo do tempo com gráficos e visualizações interativas.

 ## Simulação do Dashboard

<strong>Gráficos e Tabelas Simuladas:</strong>

1. Vendas por Concessionária:
- Gráfico de barras mostrando o número total de vendas por cada concessionária.
- Tabela detalhando o desempenho de cada concessionária.

2. Vendas por Veículo:
- Gráfico de barras ou pizza mostrando a distribuição de vendas por modelo de veículo.
- Tabela listando os modelos de veículos mais vendidos.

3. Vendas por Vendedor:
- Gráfico de barras mostrando o desempenho individual de cada vendedor.
- Tabela com detalhes das vendas realizadas por cada vendedor.
  
4. Análise Temporal:
- Gráfico de linha mostrando as tendências de vendas ao longo do tempo.
- Análise de sazonalidade e picos de vendas em determinados períodos.

## Método de LT (Load Transform)


Utilizamos o método de LT (Load Transform) para carregar os dados brutos diretamente no data warehouse (Snowflake) e, em seguida, realizar as transformações necessárias utilizando DBT. Esse método nos permite manter a integridade dos dados brutos enquanto aplicamos transformações para análise e relatórios.

## Estrutura do Projeto no DBT(data build tool)

```plaintext
├── data
│   ├── raw_data.sql
│   ├── transformed_data.sql
├── airflow
│   ├── dags
│   │   ├── etl_pipeline.py
├── dbt
│   ├── models
│   │   ├── analysis
│   │   │   ├── analise_venda_temporal.sql
│   │   │   ├── analise_vendas_concessionaria.sql
│   │   │   ├── analise_vendas_veiculos.sql
│   │   │   ├── analise_vendas_vendedor.sql
│   │   ├── dimensions
│   │   │   ├── dim_cidades.sql
│   │   │   ├── dim_clientes.sql
│   │   │   ├── dim_concessionarias.sql
│   │   │   ├── dim_estados.sql
│   │   │   ├── dim_veiculos.sql
│   │   │   ├── dim_vendedores.sql
│   │   ├── facts
│   │   │   ├── fct_vendas.sql
│   │   ├── stage
│   │   │   ├── stg_cidades.sql
│   │   │   ├── stg_clientes.sql
│   │   │   ├── stg_concessionarias.sql
│   │   │   ├── stg_estados.sql
│   │   │   ├── stg_vendas.sql
│   │   │   ├── stg_veiculos.sql
│   │   │   ├── stg_vendedores.sql
├── README.md
└── requirements.txt
