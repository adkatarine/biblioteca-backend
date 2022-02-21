from src.infra.mongodb.config.database import collection_works
from src.schemas import Work
from bson import ObjectId


class RepositoryWork:
    def __init__(self):
        self.connection = collection_works()

    def insert(self, work: Work):
        self.connection.insert_one(work.dict())

    def update(self, id: str, work: Work):
        if self.connection.find_one({"_id": ObjectId(id)}):
            self.connection.update_one({"_id": ObjectId(id)}, {"$set": work.dict()})

    def read(self):
        return self.connection.find()

    def delete(self, id: int):
        ...
