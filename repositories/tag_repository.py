from db.run_sql import run_sql

from models.merchant import *
from models.transaction import *
from models.tag import *

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository


def save(tag):
    sql = "INSERT INTO tags (name) VALUES (?) RETURNING *"
    values = [tag.tag_name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    tag.id = id
    return tag


def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row["name"], row["id"])
        tags.append(tag)
    return tags


def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        tag = Tag(result["name"], result["id"])
    return tag


def delete_all():
    sql = "DELETE  FROM tags"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM tags WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(tag):
    sql = "UPDATE tags SET (name) = (? ) WHERE id =?"
    values = [tag.tag_name, tag.id]
    run_sql(sql, values)
