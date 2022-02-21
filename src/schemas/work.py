from pydantic import BaseModel
from typing import List


class Work(BaseModel):
    """Classe utilizada para gerenciar os dados das obras no database."""

    title: str
    publishing_company: str
    photo: str
    authors: List[str] = []
