#!/usr/bin/env pyhon3
"""
Basic Babel setup
"""


from flask import Flask, request, g

app = Flask(__name__)

# Supported locales
SUPPORTED_LOCALES = ['en', 'fr']

# Default locale
DEFAULT_LOCALE = 'en'

@app.before_request
def before_request():
    # Check if locale parameter is present in the request URL
    locale = request.args.get('locale')

    if locale in SUPPORTED_LOCALES:
        # If the provided locale is supported, set it in the global g object
        g.locale = locale
    else:
        # If the locale parameter is not present or not supported, use the default locale
        g.locale = DEFAULT_LOCALE

@app.route('/')
def home():
    # Get the localized title based on the current locale
    title = get_localized_string('home_title')

    return f"<h1>{title}</h1>"

def get_localized_string(message_id):
    # Replace this function with your method of fetching localized strings based on the message_id and locale
    # You can use the gettext function or a custom translation mechanism
    # Here's a simplified example using a dictionary:
    translations = {
        'home_title': {
            'en': 'Welcome',
            'fr': 'Bienvenue'
        }
    }

    locale = g.locale  # Get the current locale from the global g object

    if message_id in translations and locale in translations[message_id]:
        return translations[message_id][locale]
    else:
        return ''

if __name__ == '__main__':
    app.run()

