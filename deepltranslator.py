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

    def get_translation_json(self, lst, source_lang=None, target_lang=None, formality=None, preserve_formatting=None,
                             split_sentences=None):

        if target_lang is None:
            target_lang = self.config["default_target_lang"]

        if source_lang is None and self.config["default_source_lang"] is not None:
            source_lang = self.config["default_source_lang"]

        if preserve_formatting is None:
            preserve_formatting = self.config["preserve_formatting"]

        if formality is None:
            formality = self.config["formality"]

        if split_sentences is None:
            split_sentences = self.config["split_sentences"]

        # Building request
        url = self.config["url"]
        data = [
            ("auth_key", self.config["auth_key"]),
            ("User-Agent", "deepl-py"),
            ("target_lang", target_lang),
            ("source_lang", source_lang),
            ("formality", formality),
            ("preserve_formatting", preserve_formatting),
            ("split_sentences", split_sentences)
        ]

        # Adding one or multiple sentences to be translated:
        for sentence in lst:
            data.append(("text", sentence))

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

    # Returns a translation for a single sentence or a list
    def get_translation(self, txt=None, lst=None, source_lang=None, target_lang=None, formality=None,
                        preserve_formatting=None,
                        split_sentences=None):
        if lst is None:
            lst = [txt]
            json_response = self.get_translation_json(lst, source_lang=source_lang, target_lang=target_lang,
                                                      formality=formality, preserve_formatting=preserve_formatting,
                                                      split_sentences=split_sentences)
            return self.process_deepl_response(json_response)[0]
        else:
            json_response = self.get_translation_json(lst, source_lang=source_lang, target_lang=target_lang,
                                                      formality=formality, preserve_formatting=preserve_formatting,
                                                      split_sentences=split_sentences)
            return self.process_deepl_response(json_response)

    # Processes a json object sent back by DeepL
    def process_deepl_response(self, deepl_response):
        if isinstance(deepl_response, requests.HTTPError):
            exit()
        translations = []
        for translation in deepl_response['translations']:
            translations.append(translation['text'])
        return translations
