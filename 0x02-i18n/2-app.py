#!/usr/bin/env python3
"""
1-app.py
"""
from flask_babel import Babel
from flask import Flask, render_template


class Config:
    """
    configuration of languages
    """

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

    return render_template('2-index.html')


# @babel.localeselector
def get_locale():
    """
    selecting the prefer language from
    the http request header by the user
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
