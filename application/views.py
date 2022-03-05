from flask import Blueprint, request, render_template

from constants import Currency, HTTPMethods, TransactionFields
from models import Transaction
from utils import get_utc_now

transactions = Blueprint("transactions", __name__)


@transactions.route("/", methods=[HTTPMethods.GET, HTTPMethods.POST])
def main():
    if request.method == HTTPMethods.POST:
        transaction = Transaction(
            value=request.form[TransactionFields.VALUE],
            currency=request.form[TransactionFields.CURRENCY],
            description=request.form[TransactionFields.DESCRIPTION],
        )

        print(transaction)

        # print(value, currency, description)

    return render_template('index.html', currencies=Currency.get_currencies())
