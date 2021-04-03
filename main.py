# Example of a simple use of the translator
import deepltranslator


translator = deepltranslator.DeeplTranslator()
print("Single sentence, using default languages:")
print(translator.get_translation("Hello"))
print("Single sentence, using languages different from default:")
print(translator.get_translation("Bonjour", source_lang='fr', target_lang='en'))
print("List of sentences:")
print(translator.get_translation(lst=["Hello", "How are you?"]))
