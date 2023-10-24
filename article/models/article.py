from pydantic import BaseModel, validator
from fastapi import HTTPException, status
from typing import List, Optional
from datetime import datetime


class Comment(BaseModel):
    user: str
    text: str


class Article(BaseModel):
    title: str
    content: str
    author: str
    comment: Optional[List[Comment]] = None

    @validator("title", "content", "author")
    def comment_must_not_be_empty(cls, value):
        if not value.strip():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Data must not be empty")
        return value


def get_not_found_response(user_id: int):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user id {user_id} not find")
