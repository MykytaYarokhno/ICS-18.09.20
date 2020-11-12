from dataclasses import dataclass
from dataclasses import field

class Translation():
    def __init_(self, english_variant, russian_variant):
        self.english_variant = english_variant
        self.russian_variant = [russian_variant]

@dataclass
class TranslationWord:
    english_variant:str
    russian_variant:str

class Interpreter():

    def __init__(self):
        self.interpreter_list = []

    def add_translation(self, translation):
        for translation_word in self.interpreter_list:
            if translation_word.english_variant == translation.english_variant:
                translation_word.russian_variant.append(translation.russian_variant)
                return

            self.interpreter_list.append(Translation(translation.english_variant, translation.russian_variant))


    def print_translation(self, english_word):
        print(f"Word in english: {english_word}")
        for translation_word in self.interpreter_list:
            if(translation_word.english_variant == english_word):
                translation_str = ""
                for russian_variant in interpreter_word.russian_values:
                    translation_str += russian_value + " "

                print(f"Translations: {translation_str}")

                return

test_words = [TranslationWord("fly", "лететь"), TranslationWord("jump", "прыгать"), TranslationWord("fly", "муха")]
interpreter = Interpreter()

for test_word in test_words:
    interpreter.add_translation(test_word)

interpreter.print_translation("fly")
