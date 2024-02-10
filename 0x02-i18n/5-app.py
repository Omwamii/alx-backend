#!/usr/bin/env python3
""" Module with Babel object instance """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _


class Config:
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Returns a user dictionary or None if id cannot be found """
    login_as = int(request.args.get('login_as'))
    if not login_as or login_as not in users.keys():
        return None
    return users[login_as]


@app.before_request
def before_request():
    """ Use get_user to find a user & set it as global flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ fn to return locale """
    lang = str(request.args.get('locale'))
    if not lang or lang not in app.config['LANGUAGES']:
        return app.config['BABEL_DEFAULT_LOCALE']
    return lang


@app.route('/')
def index():
    """ return index page """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
