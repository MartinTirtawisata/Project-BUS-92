from flask import Flask
app = Flask(__name__)
app.secret_key = 'some_random_key'

from my_app.views.views import my_app

app.register_blueprint(my_app)
