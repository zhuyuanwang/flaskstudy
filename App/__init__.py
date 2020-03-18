from flask import Flask
# from .views import init_route
# from .views import blue,second
from .views import init_view

def create_app():
    app = Flask(__name__)
    # init_route(app)
    # app.register_blueprint(blue)
    # app.register_blueprint(second)
    init_view(app)
    return app