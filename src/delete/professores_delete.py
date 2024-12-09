class ProfessorDeleter:
    """
    Classe responsável por deletar registros de professores em um banco de dados.
    """
    def __init__(self, db_path='sqlite-database/epbjc.db'):
        """
        Inicializa a classe com uma conexão ao banco de dados.
        :param database_connection: Objeto de conexão com o banco de dados.
        """
        self.db_path = db_path # Armazena a conexão com o banco de dados

    def delete_professor(self, professor_id):
        """
        Deleta um professor da tabela 'professores' com base no ID fornecido.
        :param professor_id: ID do professor a ser deletado.
        """
        try:
            # Cria um cursor para executar comandos no banco de dados
            cursor = self.db_connection.cursor()

            # Define a query de exclusão usando um placeholder (%s) para evitar SQL injection
            delete_query = "DELETE FROM professores WHERE id = %s"

            # Executa a query, passando o ID do professor como argumento
            cursor.execute(delete_query, (professor_id,))

            # Salva as mudanças no banco de dados
            self.db_connection.commit()

            # Exibe mensagem de sucesso
            print(f"Professor com ID {professor_id} deletado com sucesso.")
        
        except Exception as e:
            # Captura e exibe qualquer erro que ocorra durante o processo
            print(f"Ocorreu um erro: {e}")
        
        finally:
            # Garante que o cursor será fechado após o uso, liberando recursos
            cursor.close()
