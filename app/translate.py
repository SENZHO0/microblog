import requests
from app import app
from flask_babel import _

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')

    r = requests.get(
        'https://translation.googleapis.com/language/translate/v2',
        params={
            'q': text,
            'source': source_language,
            'target': dest_language,
            'key': app.config['MS_TRANSLATOR_KEY']
        }
    )

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['data']['translations'][0]['translatedText']
