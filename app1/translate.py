import json
import requests
from flask_babel import _
from . import app

def translate(text, source_language, dest_language):
    # FOR TESTING PURPOSES
    import time
    import random
    time.sleep(4)
    if random.random() > 0.5:
        return 'BLA BLA BLAAA {0} {1} {2}'.format(text, source_language, dest_language)
    else:
        return _('Error: the translation service is not configured.')

    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    r = requests.get(
        'https://api.microsofttranslator.com/v2/Ajax.svc'
        '/Translate?text={}&from={}&to={}'.format(
            text, source_language, dest_language
            ),
        headers=auth
        )
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
