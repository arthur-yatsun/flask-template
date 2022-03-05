from flask import Blueprint, request, render_template

from constants import Currency

transactions = Blueprint("transactions", __name__)


@transactions.route("/", methods=["GET", "POST"])
def main():
    return render_template('index.html', currencies=Currency.get_currencies())
