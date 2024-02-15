#!/usr/bin/env python3
""" Module with Babel object instance, index """
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
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request():
    """ Use get_user to find a user & set it as global flask.g.user """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """ fn to return locale """
    lang = str(request.args.get('locale'))
    if lang in app.config["LANGUAGES"]:
        return lang
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_lang = request.headers.get('locale', '') 
    if header_lang in app.config["LANGUAGES"]:
        return header_lang
    return app.config["BABEL_DEFAULT_LOCALE"]


@babel.timezoneselector
def get_timezone():
    """ Get local timezone """
    tz = str(request.args.get('timezone'))
    if tz:
        return tz
    if g.user and g.user['timezone']:
        try:
            timezone = g.user['timezone']
            pytz.timezone(timezone).zone
        except pytz.exceptions.UnknownTimezoneError:
            return app.config["BABEL_DEFAULT_TIMEZONE"]
        else:
            return timezone


@app.route('/')
def index():
    """ return index page """
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
