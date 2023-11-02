#!/usr/bin/env python3
"""
1-app.py
"""
from flask_babel import Babel, _
from flask import Flask, request, render_template


class Config:
    """configuration of the languages """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)   # loads the configuration settings
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    renders the html pages
    """

    return render_template('1-index.html')


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)