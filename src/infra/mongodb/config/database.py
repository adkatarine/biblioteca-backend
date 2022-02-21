from pymongo import MongoClient
from src.config.database import database_infos


def connect():
    """Inicia e retorna conexão com o database.

    :return:
    """
    client = MongoClient(database_infos["connection_url"])
    db = client[database_infos["database"]]
    return db


def collection_works():
    """Cria e/ou retorna collection de works.

    :return:
    """
    db = connect()
    works = db[database_infos["collection"]]
    return works
