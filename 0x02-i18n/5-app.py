#!/usr/bin/env python3
"""This module define a flask aoplication
"""
from flask import (
        Flask, render_template, request, g)
from flask_babel import Babel
from flask_babel import gettext as _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Define all configurations for the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """Get user based on the url param login_as
    """
    user_id = request.args.get("login_as", None)
    if not user_id:
        return None
    return users.get(int(user_id), None)


@app.before_request
def before_request():
    """Run before any request is processed
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Get user prefered language
    """
    locale = request.args.get('locale', None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(
            app.config["LANGUAGES"])


@app.route('/')
def home():
    """define the index page of the app
    """
    context = dict(
            home_title=_("Welcome to Holberton"),
            home_header=_("Hello world!"),
            user=g.user)
    return render_template("5-index.html", **context)
