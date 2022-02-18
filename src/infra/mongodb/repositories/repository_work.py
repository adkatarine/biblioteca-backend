from src.infra.mongodb.config.database import collection_works
from src.schemas import Work


class RepositoryWork:
    def __init__(self):
        self.connection = collection_works()

    def insert(self, work: Work):
        self.connection.insert_one(work.dict())

    def update(self, id: int):
        ...

    def read(self):
        ...

    def delete(self, id: int):
        ...
