import sqlite3  # Importa o módulo para interagir com o banco de dados SQLite

class Updateyah:
    def __init__(self, db_name='sqlite-database/epbjc.db'):
        """
        Inicializa a conexão com o banco de dados SQLite.
        :param db_name: Nome do arquivo do banco de dados (caminho relativo ou absoluto).
        """
        self.connection = sqlite3.connect(db_name)  # Estabelece uma conexão com o banco de dados
        self.cursor = self.connection.cursor()  # Cria um cursor para executar comandos SQL

    def update_data(self, aluno_id, nome=None, idade=None, curso=None):
        """
        Atualiza dados de um aluno com base no ID.
        :param aluno_id: ID do aluno a ser atualizado.
        :param nome: Novo nome do aluno (opcional).
        :param idade: Nova idade do aluno (opcional).
        :param curso: Novo curso do aluno (opcional).
        """
        update_sql = '''
        UPDATE alunos
        SET nome = COALESCE(?, nome),
            idade = COALESCE(?, idade),
            curso = COALESCE(?, curso)
        WHERE id = ?;
        '''
        try:
            # Executa o comando SQL com os valores fornecidos
            self.cursor.execute(update_sql, (nome, idade, curso, aluno_id))
            self.connection.commit()  # Salva as mudanças no banco de dados
            print("Aluno atualizado com sucesso!")
        except sqlite3.Error as e:
            # Exibe uma mensagem de erro caso algo dê errado
            print(f"Erro ao atualizar dados: {e}")

    def close(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.connection.close()  # Libera os recursos do banco de dados
