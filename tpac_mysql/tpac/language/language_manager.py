import json
import os


class LanguageManager:
    def __init__(self, default_language="pt_br"):
        self.current_language = default_language
        self.texts = {}
        self.set_language(default_language)

    def set_language(self, language):
        caminho = os.path.join(
            os.path.dirname(__file__),
            f"{language}.json"
        )

        if not os.path.exists(caminho):
            raise FileNotFoundError(
                f"Idioma '{language}' não encontrado."
            )

        with open(caminho, "r", encoding="utf-8") as arquivo:
            self.texts = json.load(arquivo)

        self.current_language = language

    def get(self, key):
        return self.texts.get(key, key)