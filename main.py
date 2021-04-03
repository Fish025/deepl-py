# Example of a simple use of the translator
import deepltranslator


translator = deepltranslator.DeeplTranslator()
print("Single sentence:")
print(translator.get_translation("Hello"))
print("List of sentences:")
print(translator.get_translation(lst=["Hello", "How are you?"]))

