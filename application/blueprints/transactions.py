import math

from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import func

from constants import HTTPMethods, TransactionFields, Currency, PAGE_SIZE
from db import DBEngine
from exceptions import FieldNotFound
from models import Transaction

transactions = Blueprint("transactions", __name__)


@transactions.route("/add", methods=[HTTPMethods.GET, HTTPMethods.POST])
def add_transaction():
    if request.method == HTTPMethods.POST:
        try:
            amount = request.form[TransactionFields.VALUE]
            currency = request.form[TransactionFields.CURRENCY]
            description = request.form[TransactionFields.DESCRIPTION]
        except KeyError as error:
            raise FieldNotFound(f"Filed form wasn't found. {error = }")

        transaction = Transaction(
            amount=amount, currency=currency, description=description)

        with DBEngine().session_scope() as session:
            session.add(transaction)

        return redirect(url_for("base.main"))

    return render_template("transactions/add.html", currencies=Currency.get_currencies())


@transactions.route("/list/", defaults={"page": 1})
@transactions.route("/list/<int:page>")
def get_transactions(page: int):

    with DBEngine().session_scope() as session:
        query_result = session.query(Transaction).offset((page - 1) * PAGE_SIZE)\
            .limit(PAGE_SIZE).all()

        count = session.query(func.count(Transaction.id)).scalar()
        session.expunge_all()

    params = dict(
        transactions=query_result,
        active_page=page,
        pages=math.ceil(count / PAGE_SIZE),
        page_size=PAGE_SIZE,
    )

    return render_template("transactions/list.html", **params)


@transactions.route("/<int:transaction_id>")
def get_transaction(transaction_id: int):
    print(transaction_id)
    with DBEngine().session_scope() as session:
        transaction = session.query(Transaction).get(transaction_id)
        session.expunge_all()

    return render_template("transactions/item.html", transaction=transaction)
