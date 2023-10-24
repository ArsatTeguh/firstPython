from pydantic import BaseModel, validator
from fastapi import HTTPException, status


class Comment(BaseModel):
    user: str
    text: str

    @validator("user", "text")
    def comment_must_not_be_empty(cls, value):
        if not value.strip():
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Data must not be empty")
        return value


def responseData(req):
    status_code = req.status_code
    data = req.json()
    data_count = len(data)
    response = {
        "status_code": status_code,
        "data_count": data_count,
        "data": data
    }
    return response


def get_not_found_response(user_id: str):
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user id {user_id} not find")
