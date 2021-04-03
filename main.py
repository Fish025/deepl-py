# Example of a simple use of the translator
import deepltranslator

translator = deepltranslator.DeeplTranslator()
print("Single sentence, using default languages:")
print(translator.get_translation("Hello"))
print("Complex request:")
print(translator.get_translation("What's up", source_lang="en", target_lang="fr", formality="less",
                                 preserve_formatting=1, split_sentences=1))
print("List of sentences:")
print(translator.get_translation(lst=["Hello", "How are you?"]))
