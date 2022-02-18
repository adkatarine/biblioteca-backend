from pymongo import MongoClient
from src.config.database import database_infos


def connect():
    client = MongoClient(database_infos["connection_url"])
    db = client[database_infos["database"]]
    return db


def collection_works():
    db = connect()
    works = db[database_infos["collection"]]
    return works
