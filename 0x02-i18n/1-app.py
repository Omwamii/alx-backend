#!/usr/env python3
""" Module with Babel object instance """
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

babel = Babel(app)

def index():
    """ return index page """
    return render_template('1-index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
