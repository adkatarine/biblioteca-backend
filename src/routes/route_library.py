from fastapi import APIRouter
from src.infra.mongodb.repositories import RepositoryWork
from src.infra.Helper.helper import helper_convert
from src.schemas import Work

router = APIRouter()


@router.get("/obras")
def read_book():
    return [helper_convert(obra) for obra in RepositoryWork().read()]


@router.post("/obras")
def insert_book(work: Work):
    RepositoryWork().insert(work)
    return {"message": "insert_book"}


@router.put("/obras/{id}")
def update_book(id: int):
    return {"message": "update_book"}


@router.delete("/obras/{id}")
def delete_book(id: int):
    return {"message": "delete_book"}
