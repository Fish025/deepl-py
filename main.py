# Example of a simple use of the translator
import deepltranslator

# Initialization
translator = deepltranslator.DeeplTranslator()

# Simplest translation, options configured in "configuration,json"
print("Single sentence, using default languages:")
print(translator.get_translation("Hello"))

# Request with all options
print("Complex request:")
print(translator.get_translation("What's up?", source_lang="en", target_lang="fr", formality="less",
                                 preserve_formatting=1, split_sentences=1))

# Request for an array
print("List of sentences:")
print(translator.get_translation(lst=["Hello", "How are you?"]))
