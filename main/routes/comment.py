from fastapi import APIRouter, status
from schemas.comment import get_not_found_response, responseData, Comment
import requests


comment = APIRouter()


@comment.get("/", status_code=status.HTTP_200_OK)
async def all():
    req = requests.get("http://127.0.0.1:8000/article")
    data = responseData(req)
    return data


@comment.get("/{id_article}", status_code=status.HTTP_200_OK)
async def getByid(id_article: str):
    req = requests.get("http://127.0.0.1:8000/article/%s" % id_article)
    if req.status_code != 200:
        raise get_not_found_response(id_article)
    data = responseData(req)
    return data


@comment.post("/comment/{id_article}", status_code=status.HTTP_201_CREATED)
async def createComment(id_article: str, comment: Comment):
    url = 'http://127.0.0.1:8000/article-comment/%s'
    req = requests.post(url % id_article, data=comment.model_dump())
    if req.status_code != 201:
        raise get_not_found_response(id_article)
    data = responseData(req)
    return data
