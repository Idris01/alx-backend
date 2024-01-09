#!/usr/bin/env python3
"""This module define a flask aoplication
"""
from flask import Flask, render_template
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


@app.route('/')
def home():
    """define the index page of the app
    """
    return render_template("1-index.html")
