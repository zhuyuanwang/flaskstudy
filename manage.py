from flask_script import Manager
from App import create_app

# app = Flask(__name__)
app = create_app()
manager = Manager(app)

# @app.route('/')
# def hello():
#     return "hello zhuyuanwang"

if __name__ == '__main__':
    # app.run()
    manager.run()