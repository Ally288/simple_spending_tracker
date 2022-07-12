from db.run_sql import run_sql

from models.merchant import *
from models.transaction import *
from models.tag import *

import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository


def save(merchant):
    sql = "INSERT INTO merchants (merchant_name, tag_id) VALUES ( ?, ?) RETURNING *"
    values = [merchant.merchant_name, merchant.merchant_tag.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    merchant.id = id
    return merchant


def select_all():
    merchants = []
    sql = "SELECT * FROM merchants"
    results = run_sql(sql)
    for row in results:
        tag = tag_repository.select(row["tag_id"])
        merchant = Merchant(row["merchant_name"], tag, row["id"])
        merchants.append(merchant)
    return merchants


def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        tag = tag_repository.select(result["tag_id"])
        merchant = Merchant(result["merchant_name"], tag, result["id"])
    return merchant


def delete_all():
    sql = "DELETE FROM merchants"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM merchants WHERE id =?"
    values = [id]
    run_sql(sql, values)


def update(merchant):
    sql = "UPDATE merchants SET (merchant_name, tag_id) = (?,? ) WHERE id =?"
    values = [merchant.merchant_name, merchant.merchant_tag.id, merchant.id]
    run_sql(sql, values)
