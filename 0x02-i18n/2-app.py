#!/usr/bin/env python3
"""This module define a flask aoplication
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Define all configurations for the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get user prefered language
    """
    return request.accept_languages.best_match(
            app.config["LANGUAGES"])


@app.route('/')
def home():
    """define the index page of the app
    """
    return render_template("2-index.html")
