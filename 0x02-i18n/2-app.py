#!/usr/bin/env python3

"""
Get locale from request
"""

from flask import Flask, request
from babel import Locale, locale_selector

app = Flask(__name__)

# Supported languages
SUPPORTED_LANGUAGES = ['en', 'fr', 'es']

# Decorator for selecting the locale
@locale_selector
def get_locale():
    # Get the accepted languages from the request
    accepted_languages = request.accept_languages

    # Loop through the accepted languages and find the best match
    for lang, _ in accepted_languages:
        # Check if the language is supported
        if lang in SUPPORTED_LANGUAGES:
            return lang

    # If no supported language is found, return the default language
    return 'en'

# Route for testing the locale
@app.route('/')
def test_locale():
    return f"Selected locale: {get_locale()}"

if __name__ == '__main__':
    app.run()

