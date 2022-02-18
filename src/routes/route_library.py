from fastapi import APIRouter

router = APIRouter()


@router.get("/obras")
def read_book():
    return {"message": "read_book"}


@router.post("/obras")
def insert_book():
    return {"message": "insert_book"}


@router.put("/obras/{id}")
def update_book(id: int):
    return {"message": "update_book"}


@router.delete("/obras/{id}")
def delete_book(id: int):
    return {"message": "delete_book"}
