import pathlib
from os import getcwd
import os
import shutil

import argostranslate.package
import argostranslate.translate

from .corrections import Corrections as corrections


class Translator:

    def __init__(self) -> None:

        installed_languages = argostranslate.translate.get_installed_languages()

        self._translators = {}
        language_codes = []

        for item in installed_languages:
            language_codes.append(item.code)

        for i in language_codes:
            for j in language_codes:
                self._translators |= {
                    f"{i}_{j}": list(
                        filter(lambda x: x.code == i, installed_languages)
                    )[0].get_translation(
                        list(filter(lambda x: x.code == j, installed_languages))[0]
                    )
                }

    def _load_model(self, from_lang: str = "fa", to_lang: str = "en"):
        package_path = pathlib.Path(
            getcwd() + f"/models/translate-{from_lang}_{to_lang}.argosmodel"
        )
        # Download model if not exists and call this method again
        if not os.path.exists(package_path):
            downloaded = self._download_model(from_lang, to_lang, package_path)
            if downloaded:
                return self._load_model(from_lang, to_lang)
            else:
                return False

        argostranslate.package.install_from_path(package_path)
        installed_languages = argostranslate.translate.get_installed_languages()
        self._translators |= {
            f"{from_lang}_{to_lang}": list(
                filter(lambda x: x.code == from_lang, installed_languages)
            )[0].get_translation(
                list(filter(lambda x: x.code == to_lang, installed_languages))[0]
            )
        }
        return True

    def _download_model(
        self,
        from_lang: str = "fa",
        to_lang: str = "en",
        package_path: str = "./models/",
    ):
        try:
            # Download and install Argos Translate package
            argostranslate.package.update_package_index()
            available_packages = argostranslate.package.get_available_packages()
            available_package = list(
                filter(
                    lambda x: x.from_code == from_lang and x.to_code == to_lang,
                    available_packages,
                )
            )[0]

            download_path = available_package.download()
            shutil.copy(download_path, package_path)
            return True
        except Exception as exc:
            return False

    @corrections.remove_duplicates
    def translate(
        self, text: str, from_lang: str = "fa", to_lang: str = "en", **kwargs
    ):
        translator = self._translators.get(f"{from_lang}_{to_lang}")
        if not translator:
            loaded = self._load_model(from_lang, to_lang)
            if loaded:
                return self.translate(text, from_lang, to_lang)
        return translator.translate(text)


translator_client = Translator()
