""" Classe para proteção das variáveis de conexão com o database. Cria um dicionário
contendo todos estes dados.

"""
from environs import Env

env = Env()
env.read_env()

database_infos = {
    "connection_url": env("CONNECTION_URL"),
    "database": env("DATABASE"),
    "collection": env("COLLECTION"),
}
