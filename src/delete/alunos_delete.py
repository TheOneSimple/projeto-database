import sqlite3  # Importa o módulo SQLite para manipular o banco de dados

class AlunoDeleter:
    def __init__(self, db_path='sqlite-database/epbjc.db'):
        """
        Inicializa a classe responsável por deletar registros na tabela 'alunos'.
        :param db_path: Caminho para o banco de dados SQLite.
        """
        self.db_path = db_path  # Define o caminho para o banco de dados

    def delete_data(self, aluno_id):
        """
        Deleta um registro na tabela 'alunos' com base no ID fornecido.
        :param aluno_id: ID do aluno a ser deletado.
        """
        try:
            # Conecta ao banco de dados
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()  # Cria um cursor para executar comandos SQL

            # Executa o comando SQL para deletar o aluno com o ID fornecido
            cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
            conn.commit()  # Salva as mudanças no banco de dados

            # Verifica se algum registro foi afetado
            if cursor.rowcount == 0:
                print(f"Nenhum aluno com ID {aluno_id} foi encontrado.")  # Caso o ID não exista
            else:
                print(f"Aluno com ID {aluno_id} deletado com sucesso.")  # Caso o registro seja deletado

        except sqlite3.Error as e:
            # Captura e exibe erros relacionados ao SQLite
            print(f"Erro ao deletar aluno: {e}")
        
        finally:
            # Garante que a conexão com o banco de dados será fechada
            if conn:
                conn.close()
