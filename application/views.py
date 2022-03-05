from flask import Blueprint, request, render_template

from constants import Currency, HTTPMethods, TransactionFields
from data_models import Transaction
from utils import get_utc_now

transactions = Blueprint("transactions", __name__)


@transactions.route("/", methods=[HTTPMethods.GET, HTTPMethods.POST])
def main():
    if request.method == HTTPMethods.POST:
        Transaction({
            TransactionFields.VALUE: request.form[TransactionFields.VALUE],
            TransactionFields.CURRENCY: request.form[TransactionFields.CURRENCY],
            TransactionFields.DESCRIPTION: request.form[TransactionFields.DESCRIPTION],
            TransactionFields.CREATED_AT: get_utc_now()
        })

        # print(value, currency, description)

    return render_template('index.html', currencies=Currency.get_currencies())
