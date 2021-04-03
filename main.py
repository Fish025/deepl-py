# Example of a simple use of the translator
import deepltranslator


translator = deepltranslator.DeeplTranslator()
translation = translator.get_translation("Hello")
print(translation[0])
print(translator.get_usage())
