import psycopg2

# Configurando conexões com os banco de dados de origem e de destino
origem_conn = psycopg2.connect(
    host='127.0.0.1',
    database='dvdrental',
    user='postgres',
    password='password'
)

destino_conn = psycopg2.connect(
    host='127.0.0.1',
    database='analytics',
    user='postgres',
    password='password',
    port='5440'
)

# Criando cursor da conexão com o banco de dados de origem
origem_cursor = origem_conn.cursor()

# Obtendo todas as tabelas do banco de origem
origem_cursor.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
todas_tabelas = origem_cursor.fetchall()

# Criando curso da conexão com o banco de destino
destino_cursor = destino_conn.cursor()

# Loop pelas tabelas para criar cada uma delas no banco de destino
for tabela in todas_tabelas:
    nome_tabela = tabela[0]

    # Query para extrair a estrutura da tabela
    query = f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{nome_tabela}'"
    origem_cursor.execute(query)
    estrutura_tabela = origem_cursor.fetchall()

    # Criando as tabelas de destino com a mesma estrutura das de origem
    query = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({','.join([f'{coluna[0]} {coluna[1]}' for coluna in estrutura_tabela])})"
    destino_cursor.execute(query)
    destino_conn.commit()

    # Query para extrair todos os dados da tabela
    query = f"SELECT * FROM {nome_tabela}"
    origem_cursor.execute(query)
    dados_tabela = origem_cursor.fetchall()

# Fazendo um loop pelos dados para inserir cada um deles na tabela de destino
    for dados in dados_tabela:
        query = f"INSERT INTO {nome_tabela} VALUES ({','.join(['%s']*len(dados))})"
        destino_cursor.execute(query, dados)

    destino_conn.commit()

# Fechando as conexões com os bancos de dados
origem_conn.close()
destino_conn.close()
