from pydantic import BaseModel
from typing import List


class Work(BaseModel):
    title: str
    publishing_company: str
    photo: str
    authors: List[str] = []
