from flask import Blueprint, request, render_template


transactions = Blueprint("transactions", __name__)


@transactions.route("/", methods=["GET", "POST"])
def main():
    return render_template('index.html')
