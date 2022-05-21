from flask import Blueprint, render_template


root = Blueprint("base", __name__)


@root.route("/")
def main():
    """Root method of the app"""
    return render_template("index.html")
