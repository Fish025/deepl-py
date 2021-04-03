# See example in main.py

import requests
import json
import os


class DeeplTranslator:

    def __init__(self):
        # Loading configuration
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + '/configuration.json') as f:
            self.config = json.load(f)

    def get_translation_json(self, txt, target_lang=None):

        if target_lang is None:
            target_lang = self.config["default_target_lang"]

        if target_lang is None and self.config["default_target_lang"] is not None :
            target_lang = self.config["default_target_lang"]

        # Building request
        url = self.config["url"]
        data = {
            "auth_key": self.config["auth_key"],
            "User-Agent": "deepl-py",
            "text": txt,
            "target_lang": target_lang
        }

        try:
            response = requests.post(url=url, data=data)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return "An error occurred:" + str(exception)

        return response.json()

    def get_usage(self):
        url = self.config["usage_url"]
        data = {
            "auth_key": self.config["auth_key"],
        }

        try:
            response = requests.post(url=url, data=data)
            response.raise_for_status()
        except requests.HTTPError as exception:
            return "An error occurred:" + str(exception)

        return response.text

    def get_translation(self, text, source_lang=None, target_lang=None):
        json_response = self.get_translation_json(text, target_lang=target_lang)
        return self.process_deepl_response(json_response)

    # Processes a json object sent back by DeepL
    def process_deepl_response(self, deepl_response):
        translations = []
        for translation in deepl_response['translations']:
            translations.append(translation['text'])
        return translations



