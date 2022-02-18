from environs import Env

env = Env()
env.read_env()

database_infos = {
    "connection_url": env("CONNECTION_URL"),
    "database": env("DATABASE"),
    "collection": env("COLLECTION"),
}
