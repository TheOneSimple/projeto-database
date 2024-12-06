import sqlite3  # Importa o módulo para trabalhar com o banco de dados SQLite

class MateriaisDatabase:
    def __init__(self, db_name='sqlite-database/epbjc.db'):
        """
        Inicializa a conexão com o banco de dados SQLite e cria a tabela 'materiais' se ela não existir.
        :param db_name: Nome do arquivo do banco de dados (caminho relativo ou absoluto).
        """
        self.connection = sqlite3.connect(db_name)  # Estabelece a conexão com o banco de dados
        self.create_table()  # Garante que a tabela 'materiais' existe ao inicializar o objeto

    def create_table(self):
        """
        Cria a tabela 'materiais' se ela não existir. A tabela contém:
        - id: chave primária (autoincrementada)
        - nome: nome do material (obrigatório)
        - descricao: descrição do material (opcional)
        - quantidade: número inteiro representando a quantidade (obrigatório)
        - preco: preço do material como número decimal (obrigatório)
        """
        with self.connection:  # Usa um gerenciador de contexto para garantir o commit automático
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS materiais (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único para cada registro
                    nome TEXT NOT NULL,  -- Nome do material (obrigatório)
                    descricao TEXT,  -- Descrição do material (opcional)
                    quantidade INTEGER NOT NULL,  -- Quantidade disponível (obrigatório)
                    preco REAL NOT NULL  -- Preço do material (obrigatório)
                )
            ''')

    def insert_data(self, nome, descricao, quantidade, preco):
        """
        Insere um novo registro na tabela 'materiais'.
        :param nome: Nome do material (obrigatório).
        :param descricao: Descrição do material (opcional).
        :param quantidade: Quantidade disponível (obrigatório).
        :param preco: Preço do material (obrigatório).
        """
        try:
            with self.connection:  # Usa um gerenciador de contexto para realizar o commit automaticamente
                self.connection.execute('''
                    INSERT INTO materiais (nome, descricao, quantidade, preco) 
                    VALUES (?, ?, ?, ?)
                ''', (nome, descricao, quantidade, preco))  # Insere os valores fornecidos na tabela
        except sqlite3.Error as e:
            # Exibe uma mensagem de erro caso algo dê errado
            print(f"Erro ao inserir dados: {e}")

    def view_table(self):
        """
        Retorna todos os registros da tabela 'materiais' como uma lista de dicionários.
        :return: Lista de dicionários representando os registros ou uma lista vazia em caso de erro.
        """
        try:
            self.connection.row_factory = sqlite3.Row  # Configura a fábrica de linhas para retornar dicionários
            cursor = self.connection.execute("SELECT * FROM materiais")  # Busca todos os registros na tabela
            return [dict(row) for row in cursor.fetchall()]  # Converte cada linha para um dicionário
        except sqlite3.Error as e:
            # Exibe uma mensagem de erro caso algo dê errado e retorna uma lista vazia
            print(f"Erro ao buscar dados: {e}")
            return []

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.connection.close()  # Libera os recursos do banco de dados
