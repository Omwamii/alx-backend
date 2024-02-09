#!/usr/bin/env python3
""" Module with Babel object instance """
from flask import Flask, render_template
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
    """ Get locale function """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    """ return index page """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
