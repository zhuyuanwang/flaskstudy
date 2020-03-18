from flask import Blueprint

third = Blueprint("Third",__name__)

@third.route('/third/')
def hello():
    return "Third blue"