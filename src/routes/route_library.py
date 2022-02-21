from fastapi import APIRouter, status, HTTPException
from src.infra.mongodb.repositories import RepositoryWork
from src.schemas import Work

router = APIRouter()


@router.get("/obras")
def read_book():
    obras = RepositoryWork().read()
    if not obras:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Não há obras cadastradas."
        )
    return obras


@router.post("/obras", status_code=status.HTTP_201_CREATED)
def insert_book(work: Work):
    try:
        RepositoryWork().insert(work)
        return {"message": "Obra cadastrada com sucesso."}
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao cadastrar obra."
        )


@router.put("/obras/{id}")
def update_book(id: str, work: Work):
    try:
        RepositoryWork().update(id, work)
        return {"message": "Obra atualizada com sucesso."}
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao atualizar obra."
        )


@router.delete("/obras/{id}")
def delete_book(id: str):
    try:
        RepositoryWork().delete(id)
        return {"message": "Obra excluida com sucesso."}
    except:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Erro ao excluir obra."
        )
