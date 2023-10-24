from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from models.article import Article, get_not_found_response, Comment
from config.db import connection
from schemas.article import articlesEntity, articleEntity

from bson import ObjectId


article = APIRouter()


@article.get("/article", status_code=status.HTTP_200_OK)
async def all():
    return articlesEntity(connection.find())


@article.get("/article/{id_article}", status_code=status.HTTP_200_OK)
async def getOneArticle(id_article: str):
    article_id = ObjectId(id_article)
    new_article = connection.find_one({"_id": article_id})

    if new_article is None:
        raise get_not_found_response(id_article)

    else:
        return articleEntity(new_article)


@article.post("/article", status_code=status.HTTP_201_CREATED)
async def create(article: Article):

    jsonResult = jsonable_encoder(article)
    result = connection.insert_one(jsonResult)

    new_article = connection.find_one({"_id": result.inserted_id})

    return articleEntity(new_article)


@article.put("/article/{id_article}", status_code=status.HTTP_201_CREATED)
async def putArticle(article: dict, id_article: str):
    article_id = ObjectId(id_article)
    existing_article = connection.find_one({"_id": article_id})

    if existing_article is None:
        raise get_not_found_response(id_article)

    else:
        connection.update_one(
            {"_id": article_id}, {"$set": article})
        return {"detail": "sucsess update data"}


@article.delete("/article/{id_article}", status_code=status.HTTP_202_ACCEPTED)
async def deleteArticle(id_article: str):
    article_id = ObjectId(id_article)
    result = connection.delete_one({"_id": article_id})

    if result.deleted_count == 1:
        return {"detail": "Success Delete"}
    else:
        raise get_not_found_response(id_article)


@article.post("/article-comment/{id_article}", status_code=status.HTTP_201_CREATED)
async def addCommentArticle(id_article: str,  comment: Comment):

    article_id = ObjectId(id_article)

    exist_article = connection.find_one({"_id": article_id})
    if exist_article is None:
        raise get_not_found_response(id_article)

    exist_article["comment"].append(comment.model_dump())

    connection.update_one({"_id": article_id}, {"$set": exist_article})
    return {"detail": "Success create new comment"}
