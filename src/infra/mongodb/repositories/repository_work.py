from src.infra.mongodb.config.database import collection_works
from src.infra.helper.helper import helper_convert
from src.schemas import Work
from bson import ObjectId
from typing import List


class RepositoryWork:
    """Classe CRUD das obras no database."""

    def __init__(self):
        """Conexão com o database."""
        self.connection = collection_works()

    def insert(self, work: Work):
        """Insere uma nova obra no database.

        :param work: dados da obra.
        :return: None
        """
        self.connection.insert_one(work.dict())

    def update(self, id: str, work: Work):
        """Atualiza os dados de uma obra.

        :param id: id da obra
        :param work: dados atualizados da obra.
        :return: None
        """
        if self.connection.find_one({"_id": ObjectId(id)}):
            self.connection.update_one({"_id": ObjectId(id)}, {"$set": work.dict()})

    def read(self) -> List[dict]:
        """Retorna todas as obras cadastradas.

        :return: List[dict]
        """
        return [helper_convert(obra) for obra in self.connection.find()]

    def delete(self, id: str):
        """Exclui uma obra do database.

        :param id: id da obra.
        :return: None
        """
        if self.connection.find_one({"_id": ObjectId(id)}):
            self.connection.delete_one({"_id": ObjectId(id)})
