import unittest
from .translator import Translator


class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_translation(self):
        text = "سلام"
        result = self.translator.translate(text)
        self.assertIn("Hello", result)  # Assuming the translation is correct

    def test_duplications_in_translation(self):
        text = "خانه"
        result = self.translator.translate(text)
        self.assertEqual("Home", result)

    def test_model_loading(self):
        result = self.translator._load_model("en", "fr")
        self.assertTrue(result)

    def test_model_downloading(self):
        result = self.translator._download_model("en", "es")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
