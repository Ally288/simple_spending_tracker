from flask import Flask, render_template, request, redirect
from flask import Blueprint
import datetime

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

transaction_blueprint = Blueprint("transactions", __name__)


@transaction_blueprint.route("/home")
def home():
    return render_template("index.html")


@transaction_blueprint.route("/contact")
def contact():
    return render_template("contact.html")


@transaction_blueprint.route("/about")
def about():
    return render_template("about.html")


@transaction_blueprint.route("/cookie-policy")
def cookie_policy():
    return render_template("cookie_policy.html")


@transaction_blueprint.route("/legal-information")
def legal_information():
    return render_template("legal_info.html")


# user can view transactions & total amount spent
@transaction_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    transactions.sort(key=lambda trans: trans.transaction_date)
    total = 0.00
    for transaction in transactions:
        total += round(transaction.transaction_amount, 2)
    return render_template(
        "transactions/index.html", all_transactions=transactions, total=total
    )


# user adds new transaction
@transaction_blueprint.route("/add-transaction", methods=["GET"])
def new_transaction():
    transactions = transaction_repository.select_all()
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template(
        "transactions/add_transaction.html",
        all_transactions=transactions,
        all_merchants=merchants,
        all_tags=tags,
    )


# creates new transaction
@transaction_blueprint.route("/add-transaction", methods=["POST"])
def add_transaction():
    date = request.form["date"]
    split_date = date.split("-")
    print(split_date)
    date = datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    merchant = merchant_repository.select(request.form["merchant_id"])
    tag = tag_repository.select(request.form["tag_id"])
    amount = request.form["amount"]
    transaction = Transaction(date, merchant, tag, amount)
    transaction_repository.save(transaction)
    return redirect("/transactions")


@transaction_blueprint.route("/budgeting")
def budgeting():
    return render_template("transactions/budgeting.html")
