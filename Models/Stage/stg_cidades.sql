{{ config(materialized='view') }} -- vai interpretado quado esse codigo for executado
WITH source AS ( -- dizendo que todas as minhas colunas serão armazenado dentro desse source
    SELECT 
        id_cidades,
        INITCAP(cidade) AS nome_cidade, 
        id_estados,
        data_inclusao,
        COALESCE(data_atualizacao, data_inclusao) AS data_atualizacao  -- o COALESCE será muito util trtar valores que são nulo
    FROM {{ source('sources', 'cidades') }}
)

SELECT
    id_cidades,
    nome_cidade,
    id_estados,
    data_inclusao,
    data_atualizacao
FROM source
