class MaterialRepository:
    """
    Classe que representa um repositório de materiais em memória.
    Permite adicionar, deletar e listar materiais armazenados.
    """
    def __init__(self, db_path='sqlite-database/epbjc.db'):
        """
        Inicializa o repositório com uma lista vazia de materiais.
        """
        self.db_path = db_path
        self.materials = []  # Lista que armazena os materiais

    def add_material(self, material):
        """
        Adiciona um material ao repositório.
        :param material: Objeto que representa um material.
        """
        self.materials.append(material)  # Adiciona o material à lista

    def delete_material(self, material_id):
        """
        Remove um material do repositório com base no ID.
        :param material_id: Identificador único do material a ser removido.
        """
        # Filtra a lista de materiais para remover aquele cujo ID corresponde ao fornecido
        self.materials = [material for material in self.materials if material.material_id != material_id]

    def get_all_materials(self):
        """
        Retorna todos os materiais no repositório.
        :return: Lista de materiais.
        """
        return self.materials  # Retorna a lista completa de materiais

# Exemplo de uso
if __name__ == "__main__":
    # Instancia o repositório
    repo = MaterialRepository()

    # Aqui seria possível adicionar lógica para criar objetos de material
    # e manipulá-los com os métodos da classe.
