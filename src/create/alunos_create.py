import sqlite3  # Importa o módulo para interagir com o banco de dados SQLite

class AlunosDatabase:
    def __init__(self, db_name='sqlite-database/epbjc.db'):
        """
        Inicializa a conexão com o banco de dados SQLite e cria a tabela se não existir.
        :param db_name: Nome do arquivo do banco de dados (caminho relativo ou absoluto).
        """
        self.connection = sqlite3.connect(db_name)  # Estabelece uma conexão com o banco de dados
        self.cursor = self.connection.cursor()  # Cria um cursor para executar comandos SQL
        self.create_table()  # Garante que a tabela "alunos" existe ao inicializar o objeto

    def create_table(self):
        """
        Cria a tabela 'alunos' se ela não existir. A tabela contém:
        - id: chave primária (autoincrementada)
        - nome: texto obrigatório
        - idade: número inteiro
        - curso: texto
        """
        create_table_sql = '''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único para cada registro
            nome TEXT NOT NULL,  -- Nome do aluno (obrigatório)
            idade INTEGER,  -- Idade do aluno (opcional)
            curso TEXT  -- Nome do curso (opcional)
        );
        '''
        self.cursor.execute(create_table_sql)  # Executa o comando SQL para criar a tabela
        self.connection.commit()  # Salva as mudanças no banco de dados

    def insert_data(self, nome, idade, curso):
        """
        Insere um novo registro na tabela 'alunos'.
        :param nome: Nome do aluno (obrigatório).
        :param idade: Idade do aluno (opcional).
        :param curso: Nome do curso do aluno (opcional).
        """
        try:
            insert_sql = '''
            INSERT INTO alunos (nome, idade, curso) 
            VALUES (?, ?, ?);
            '''
            # Executa o comando SQL com os valores fornecidos
            self.cursor.execute(insert_sql, (nome, idade, curso))
            self.connection.commit()  # Salva as mudanças no banco de dados
        except sqlite3.Error as e:
            # Exibe uma mensagem de erro caso algo dê errado
            print(f"Erro ao inserir dados: {e}")

    def view_table(self):
        """
        Retorna todos os registros da tabela 'alunos'.
        :return: Uma lista de tuplas com os registros.
        """
        try:
            self.cursor.execute("SELECT * FROM alunos")  # Executa um comando SQL para buscar todos os registros
            return self.cursor.fetchall()  # Retorna os resultados como uma lista de tuplas
        except sqlite3.Error as e:
            # Exibe uma mensagem de erro caso algo dê errado e retorna uma lista vazia
            print(f"Erro ao buscar dados: {e}")
            return []

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.connection.close()  # Libera os recursos do banco de dados
