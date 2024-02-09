#!/usr/env python3
""" Module with Babel object instance """
from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


class Config(Babel):
    """ Config class for languages """
    LANGUAGES = ["en", "fr"]
    def __init__(se;f, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def default_locale():
        """ default locale for app """
        return Config.LANGUAGES[0]

babel = Config(app)
