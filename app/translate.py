import json

import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if (
        "MS_TRANSLATOR_KEY" not in current_app.config
        or not current_app.config["MS_TRANSLATOR_KEY"]
    ):
        return _("Error: the translation service is not configured.")
    auth = {"Ocp-Apim-Subscription-Key": current_app.config["MS_TRANSLATOR_KEY"]}
    ms_translate_ml_api = f"https://api.microsofttranslator.com/v2/Ajax.svc/Translate?text={text}&from={source_language}&to={dest_language}"
    response = requests.get(ms_translate_ml_api, headers=auth)
    if response.status_code != 200:
        return _("Error: the translation service failed.")
    return json.loads(response.content.decode("utf-8-sig"))
