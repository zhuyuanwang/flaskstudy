# def init_route(app):
#     @app.route('/')
#     def hello():
#         return 'hello zhuyuanwang0217'
#
#     @app.route('/index/')
#     def index():
#         print('This is index')
#         return "这是首页"

# from flask import Blueprint
#
# blue = Blueprint('blue',__name__)
#
# @blue.route('/')
# def index():
#     return "This is blueprint index"
from .first_blue import blue
from .second_blue import second
from .third_blue import third

def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)