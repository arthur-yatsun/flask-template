from flask import Blueprint, render_template, request, redirect, url_for

from constants import HTTPMethods, TransactionFields, Currency
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

    return render_template('transactions/add.html', currencies=Currency.get_currencies())


@transactions.route("/list")
def get_all_transactions():
    pass


@transactions.route("/")
def get_transaction():
    pass
