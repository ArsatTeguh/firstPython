from typing import List


def commentEntity(comment_list: List[dict]):
    return [
        {"user": comment["user"], "text": comment["text"]} for comment in comment_list
    ]


def articleEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "content": item["content"],
        "author": item["author"],
        "comment": commentEntity(item.get("comment", []))
    }


def articlesEntity(entity) -> list:
    return [articleEntity(item) for item in entity]
