#!/usr/bin/env python3
"""This module define a flask aoplication
"""
from flask import (
        Flask, render_template,
        request, g, Response)
from flask_babel import Babel
from flask_babel import gettext as _
from typing import Dict, Union
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError

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


def get_user() -> Union[Dict, None]:
    """Get user based on the url param login_as
    """
    user_id = request.args.get("login_as", None)
    if not user_id:
        return None
    return users.get(int(user_id), None)


@app.before_request
def before_request() -> None:
    """Run before any request is processed
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Get user prefered language
    """
    locale = request.args.get('locale', None)
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    user = g.user
    if user:
        locale = user.get("locale")
        if locale in app.config["LANGUAGES"]:
            return locale

    return request.accept_languages.best_match(
            app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """Get user timezone
    """
    timez = request.args.get('timezone', "")
    try:
        timezone(timez)
        return timez
    except UnknownTimeZoneError:
        pass

    try:
        user = g.user
        if user:
            timez = timezone(user.timezone)
            return timez
    except UnknownTimeZoneError:
        pass

    return None


@app.route('/')
def home() -> Response:
    """define the index page of the app
    """
    context = dict(
            home_title=_("Welcome to Holberton"),
            home_header=_("Hello world!"),
            user=g.user)
    return render_template("6-index.html", **context)
