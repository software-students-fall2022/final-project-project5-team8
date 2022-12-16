from PIL import Image
from pytesseract import pytesseract
import translate


class Tests:
    def sanity_check(self):
        """
        Test system sanity to ensure logic is properly implemented.
        """
        expected = True
        actual = True
        assert actual == expected, "Expected True to be equal to True!"

    def test_translate(self):
        """
        Test that translate() in translate.py returns the correct translated text
        per Google Translate.
        """
        input = "The quick brown fox jumps over the lazy dog."

        lang1 = translate.translate(input, "en", "es")
        lang2 = translate.translate(input, "en", "fr")
        lang3 = translate.translate(input, "en", "de")

        exp1 = "El veloz zorro marrón salta sobre el perro perezoso."
        exp2 = "Le renard brun rapide saute par-dessus le chien paresseux."
        exp3 = "Der schnelle braune Fuchs springt über den faulen Hund."

        assert lang1 == exp1, "Expected Spanish translation to be correct!"
        assert lang2 == exp2, "Expected French translation to be correct!"
        assert lang3 == exp3, "Expected German translation to be correct!"

    def img_to_text(self):
        """
        Test that img_to_text() in img_translation.py returns the correct text
        per the image.
        """
        img = Image.open("machine-learning-client/tests/test.png")
        text = pytesseract.image_to_string(img)
        expected = "Sample Text 3"
        assert text == expected, "Expected extracted text to be correct!"
