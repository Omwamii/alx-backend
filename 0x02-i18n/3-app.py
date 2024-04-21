#!/usr/bin/env python3
""" Module with Babel object instance """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ fn to return locale """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ return index page """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
