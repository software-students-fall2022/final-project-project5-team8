import unittest
from langdetect import detect, DetectorFactory
from chatbot import get_response



class Test_chatbot(unittest.TestCase):
    def test_get_response_Chinese(self):
        answer_chi,answer_eng=get_response("今天天气真不错","Chinese")
        DetectorFactory.seed=0
        lang1=detect(answer_chi)
        lang2=detect(answer_eng)
        self.assertTrue(lang1=="zh-cn")
        self.assertTrue(lang2=="en")

    def test_get_response_French(self):
        answer_fr,answer_eng=get_response("Où puis-je trouver un bon restaurant?","French")
        DetectorFactory.seed=0
        lang1=detect(answer_fr)
        lang2=detect(answer_eng)
        self.assertTrue(lang1=="fr")
        self.assertTrue(lang2=="en")

    def test_get_response_Spanish(self):
        answer_jp,answer_eng=get_response("しけんはかんたんでした","Japanese")
        DetectorFactory.seed=0
        lang1=detect(answer_jp)
        lang2=detect(answer_eng)
        self.assertTrue(lang1=="ja")
        self.assertTrue(lang2=="en")
