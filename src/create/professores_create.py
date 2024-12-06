import sqlite3  # Importa o módulo SQLite para manipular o banco de dados

class ProfessoresDB:
    def __init__(self, db_name='sqlite-database/epbjc.db'):
        """
        Inicializa a conexão com o banco de dados SQLite e cria a tabela 'professores' se ela não existir.
        :param db_name: Caminho para o arquivo do banco de dados (relativo ou absoluto).
        """
        self.connection = sqlite3.connect(db_name)  # Conecta ao banco de dados SQLite
        self.cursor = self.connection.cursor()  # Cria um cursor para executar comandos SQL
        self.create_table()  # Garante que a tabela 'professores' existe ao inicializar o objeto

    def create_table(self):
        """
        Cria a tabela 'professores' se ela não existir. A tabela contém:
        - id: chave primária (autoincrementada)
        - nome: texto obrigatório representando o nome do professor
        - departamento: texto obrigatório representando o departamento do professor
        - email: texto obrigatório e único para identificar o professor
        """
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único (autoincrementado)
            nome TEXT NOT NULL,  -- Nome do professor (obrigatório)
            departamento TEXT NOT NULL,  -- Departamento do professor (obrigatório)
            email TEXT UNIQUE NOT NULL  -- Email único do professor (obrigatório)
        );
        '''
        self.cursor.execute(create_table_sql)  # Executa o comando SQL para criar a tabela
        self.connection.commit()  # Salva as mudanças no banco de dados

    def insert_data(self, nome, departamento, email):
        """
        Insere um novo registro na tabela 'professores'.
        :param nome: Nome do professor (obrigatório).
        :param departamento: Departamento do professor (obrigatório).
        :param email: Email do professor (obrigatório e único).
        """
        try:
            insert_sql = '''
            INSERT INTO professores (nome, departamento, email)
            VALUES (?, ?, ?);
            '''
            # Executa o comando SQL de inserção com os valores fornecidos
            self.cursor.execute(insert_sql, (nome, departamento, email))
            self.connection.commit()  # Salva as mudanças no banco de dados
        except sqlite3.IntegrityError as e:
            # Captura erros de integridade, como violação de unicidade do email
            print(f"Erro ao inserir dados (provavelmente email duplicado): {e}")
        except sqlite3.Error as e:
            # Captura outros erros relacionados ao SQLite
            print(f"Erro ao inserir dados: {e}")

    def view_table(self):
        """
        Retorna todos os registros da tabela 'professores'.
        :return: Lista de tuplas contendo os registros ou uma lista vazia em caso de erro.
        """
        try:
            self.cursor.execute("SELECT * FROM professores")  # Busca todos os registros da tabela
            return self.cursor.fetchall()  # Retorna os resultados como uma lista de tuplas
        except sqlite3.Error as e:
            # Captura e exibe erros ao buscar os dados, retornando uma lista vazia
            print(f"Erro ao buscar dados: {e}")
            return []

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.connection.close()  # Libera os recursos associados ao banco de dados
