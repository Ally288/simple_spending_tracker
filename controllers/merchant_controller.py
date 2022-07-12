from flask import Flask, render_template, request, redirect
from flask import Blueprint
import datetime

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag

import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

merchant_blueprint = Blueprint("merchant", __name__)

# view merchants
@merchant_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchant/show.html", all_merchants=merchants)


# show individual merchant
@merchant_blueprint.route("/merchant/<id>", methods=["GET"])
def show_merchant(id):
    merchant = merchant_repository.select(id)
    tag = tag_repository.select(id)
    return render_template("merchant/show.html", merchant=merchant, tag=tag)


# user adds a merchant
@merchant_blueprint.route("/create-merchant", methods=["GET"])
def add_merchant():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template(
        "merchant/create.html", all_merchants=merchants, all_tags=tags
    )


# create merchant
@merchant_blueprint.route("/create-merchant", methods=["POST"])
def create_merchant():
    name = request.form["merchant_name"]
    new_tag = tag_repository.select(request.form["tag_id"])
    updated_tag = tag_repository.save(new_tag)
    new_merchant = Merchant(name, updated_tag)
    merchant_repository.save(new_merchant)
    return redirect("/merchants")


# allows user to amend a merchant
@merchant_blueprint.route("/merchant/<id>/amend-merchant", methods=["GET"])
def amend_merchant(id):
    merchant = merchant_repository.select(id)
    tag = tag_repository.select_all()
    transactions = transaction_repository.select_all()
    return render_template(
        "merchant/amend.html",
        merchant=merchant,
        all_tags=tag,
        all_transactions=transactions,
    )


# updates merchant
@merchant_blueprint.route("/merchant/<id>/amend-merchant", methods=["POST"])
def update_merchant(id):
    name = request.form["merchant-name"]
    tag_id = request.form["merchant-tag"]
    tag = tag_repository.select(tag_id)
    merchant_name_update = Merchant(name, tag, id)
    merchant_repository.update(merchant_name_update)
    return redirect("/merchants")
