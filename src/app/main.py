import sys
import os

# Adiciona o diretório pai ao sys.path para permitir importações de outros diretórios
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as classes para manipulação de tabelas
from create.alunos_create import AlunosDatabase  # Classe para manipular a tabela 'alunos'
from create.professores_create import ProfessoresDB  # Classe para manipular a tabela 'professores'
from create.materiais_create import MateriaisDatabase  # Classe para manipular a tabela 'materiais'
from delete.alunos_delete import AlunoDeleter  # Classe para deletar registros na tabela 'alunos'
from delete.materiais_delete import MaterialRepository  # Classe para deletar registros na tabela 'materiais'
from delete.professores_delete import ProfessorDeleter  # Classe para deletar registros na tabela 'professores'

def main():
    """
    Função principal que apresenta um menu de gerenciamento para o banco de dados.
    Permite inserir, visualizar e deletar registros das tabelas 'alunos', 'professores' e 'materiais'.
    """
    print("Bem-vindo ao Sistema de Gerenciamento de Banco de Dados")
    db_name = 'sqlite-database/epbjc.db'  # Caminho para o banco de dados SQLite

    try:
        while True:
            # Exibe o menu principal
            print("\nMenu Principal:")
            print("1. Inserir dados na tabela Alunos")
            print("2. Inserir dados na tabela Professores")
            print("3. Inserir dados na tabela Materiais")
            print("4. Visualizar tabelas")
            print("5. Remover dados")
            print("6. Sair")
            choice = input("Escolha uma opção: ")

            # Opção 5: Remover dados
            if choice == '5':
                print("\nEscolha uma tabela para deletar dados:")
                print("1. Alunos")
                print("2. Professores")
                print("3. Materiais")
                table_choice = input("Escolha uma opção: ")

                if table_choice == '1':  # Deletar dados da tabela 'alunos'
                    db = AlunoDeleter(db_name)
                    aluno_id = int(input("Digite o ID do aluno a ser deletado: "))
                    db.delete_data(aluno_id)
                    print("Aluno deletado com sucesso!")
                    db.close()
                elif table_choice == '2':  # Deletar dados da tabela 'professores'
                    db = ProfessorDeleter(db_name)
                    professor_id = int(input("Digite o ID do professor a ser deletado: "))
                    db.delete_data(professor_id)
                    print("Professor deletado com sucesso!")
                    db.close()
                elif table_choice == '3':  # Deletar dados da tabela 'materiais'
                    db = MaterialRepository(db_name)
                    material_id = int(input("Digite o ID do material a ser deletado: "))
                    db.delete_data(material_id)
                    print("Material deletado com sucesso!")
                    db.close()
                else:
                    print("Opção inválida.")

            # Opção 2: Inserir dados na tabela 'professores'
            elif choice == '2':
                db = ProfessoresDB(db_name)
                nome = input("Digite o nome do professor: ")
                departamento = input("Digite o departamento do professor: ")
                email = input("Digite o email do professor: ")
                db.insert_data(nome, departamento, email)
                print("Professor inserido com sucesso!")
                db.close()

            # Opção 3: Inserir dados na tabela 'materiais'
            elif choice == '3':
                db = MateriaisDatabase(db_name)
                nome = input("Digite o nome do material: ")
                descricao = input("Digite a descrição do material: ")
                quantidade = int(input("Digite a quantidade do material: "))
                preco = float(input("Digite o preço do material: "))
                db.insert_data(nome, descricao, quantidade, preco)
                print("Material inserido com sucesso!")
                db.close()

            # Opção 4: Visualizar tabelas
            elif choice == '4':
                print("\nEscolha uma tabela para visualizar:")
                print("1. Alunos")
                print("2. Professores")
                print("3. Materiais")
                table_choice = input("Escolha uma opção: ")

                if table_choice == '1':  # Visualizar tabela 'alunos'
                    db = AlunosDatabase(db_name)
                    data = db.view_table()
                    print("\nTabela Alunos:")
                    for row in data:
                        print(row)
                    db.close()
                elif table_choice == '2':  # Visualizar tabela 'professores'
                    db = ProfessoresDB(db_name)
                    data = db.view_table()
                    print("\nTabela Professores:")
                    for row in data:
                        print(row)
                    db.close()
                elif table_choice == '3':  # Visualizar tabela 'materiais'
                    db = MateriaisDatabase(db_name)
                    data = db.view_table()
                    print("\nTabela Materiais:")
                    for row in data:
                        print(row)
                    db.close()
                else:
                    print("Opção inválida.")

            # Opção 6: Sair do programa
            elif choice == '6':
                print("Encerrando o programa...")
                break

            # Caso nenhuma das opções seja válida
            else:
                print("Opção inválida. Tente novamente.")
    except Exception as e:
        # Captura e exibe erros gerais
        print(f"Ocorreu um erro: {e}")
        print("Encerrando o programa...")

if __name__ == "__main__":
    main()  # Executa o programa principal
