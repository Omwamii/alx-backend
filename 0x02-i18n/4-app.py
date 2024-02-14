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
def get_locale() -> str:
    """ fn to return locale """
    lang = str(request.args.get('locale'))
    if not lang or lang not in app.config['LANGUAGES']:
        return app.config['BABEL_DEFAULT_LOCALE']
    return lang


@app.route('/')
def index() -> str:
    """ return index page """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
