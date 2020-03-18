from flask import Blueprint

blue = Blueprint('blue',__name__)

@blue.route('/')
def index():
    return "This is blueprint index123"