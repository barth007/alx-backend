#!/usr/bin/env python3
from flask import Flask, render_template
"""
0-app.py
"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """
    This renders an html page
    """

    return render_template('0-index.html')


if __name__ == "__main__":
    """Entry point Main"""

    app.run(host='0.0.0.0', port=5000, debug=True)
