from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.providers.snowflakes.hooks.snowflakes import SnowflakeHook

default_args = {

    'owner' : 'airflow',
    'depends_on_past' : False,
    'start_date': datetime(2024,1,1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,  # Aqui servi pra dizer quantas vezes task tem que tentar caso tiver uma falha
    'retry_delay': timedelta(min = 5), # aqui servi pra dizer quanto tempo será pra tentar de novo caso tiver uma falha

}

@dag( # definição da minha DAG

    dag_id='postgres_to_snowflake',
    default_args = default_args,
    description = 'Load data incrementally from postgres to snowflake',
    schedule_interval = timedelta (days = 1),
    catchup = False # vai exercuta todos os processo que não foram executado
)

def postgre_to_snowflake_etl():
    table_names = ['veiculos', 'estados', 'cidades', 'concessionarias', 'vendedores', 'clientes','vendas'] #aqui vai pegar todos os nomes do meu banco de dados relacional

    for table_name in table_names:
        @task(task_id= f'get_max_id_{table_name}')
        def get_max_primary_key(table_name: str):
            with SnowflakeHook(snowflake_conn_id= 'snowflake').get_conn() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(f'SELECT MAX(ID_{table_name}) FROM {table_name}')
                    max_id = cursor.fetchone()[0]
                    return max_id if max_id is not None else 0
        @task(task_id = f'load_data_{table_name}')
        def load_incremental_data(table_name: str,max_id:int):
            with PostgresHook(postgres_conn_id='postgres').get_conn() as pg_conn:
                with pg_conn.cursor() as pg_cursor:
                    primary_key = f'ID_{table_name}'

                    pg_cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'")
                    columns = [row[0] for row in pg_cursor.fetchall()]
                    columns_list_str = ', '.join(columns)
                    placeholders = ', '.join(['%s'] * len(columns)) # insert into veiculos, venda, estado (%,%,%,% ...)

                    pg_cursor.execute(f"SELECT {columns_list_str} FROM {table_name} WHERE {primary_key} > {max_id}")
                    rows = pg_cursor.fetchall()

                    with SnowflakeHook(snowflake_conn_id = 'snowflake').get_conn() as sf_conn:
                        with sf_conn.cursor() as sf_cursor:
                            insert_querry= f"INSERT INTO {table_name} ({columns_list_str}) VALUES ({placeholders})"
                            for row in rows:
                                sf_cursor.execute(insert_querry, row)
        max_id = get_max_primary_key(table_name)
        load_incremental_data(table_name, max_id)

postgre_to_snowflake_etl_dag = postgre_to_snowflake_etl()