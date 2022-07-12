from db.run_sql import run_sql

from models.merchant import *
from models.transaction import *
from models.tag import *
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository


def save(transaction):
    sql = "INSERT INTO transactions (transaction_date, transaction_amount, tag_id, merchant_id) VALUES (?, ?, ?, ?) RETURNING *"
    values = [
        transaction.transaction_date,
        transaction.transaction_amount,
        transaction.tag.id,
        transaction.merchant.id,
    ]
    results = run_sql(sql, values)
    id = results[0]["id"]
    transaction.id = id
    return transaction


def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row["tag_id"])
        merchant = merchant_repository.select(row["merchant_id"])
        transaction = Transaction(
            row["transaction_date"], merchant, tag, row["transaction_amount"]
        )
        transactions.append(transaction)
    return transactions


def select(id):
    transaction = None
    sql = "SELECT * FROM transactions WHERE id =?"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        merchant = merchant_repository.select(result["merchant_id"])
        tag = tag_repository.select(result["tag_id"])
        transaction = Transaction(
            result["transaction_date"], merchant, tag, result["transaction_amount"]
        )
    return transaction


def delete_all():
    sql = "DELETE  FROM transactions"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM transactions WHERE id = ?"
    values = [id]
    run_sql(sql, values)


def update(transaction):
    sql = "UPDATE transactions SET (transaction_date, transaction_amount, tag_id, merchant_id) = (?, ?, ?, ? ) WHERE id =?"
    values = [
        transaction.transaction_date,
        transaction.transaction_amount,
        transaction.tag.id,
        transaction.merchant.id,
    ]
    run_sql(sql, values)
