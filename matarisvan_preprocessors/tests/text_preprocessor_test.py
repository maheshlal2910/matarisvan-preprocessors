import unittest

from matarisvan_preprocessors.text_preprocessors import TextExtractor, StringPreprocessor

class TextExtractorTest(unittest.TestCase):
    
    def test_should_get_text_from_html(self):
        text_extractor = TextExtractor()
        html = """<html> <body> hello world </body> </html>"""
        text = """hello world"""
        self.assertEquals(text.replace('\n', ''), text_extractor.process(html))


class StringPreprocessorTest(unittest.TestCase):

    def test_should_convert_numeric_to_string(self):
        string_preprocessor = StringPreprocessor()
        self.assertEquals('123', string_preprocessor.process(123))

    def test_should_convert_string_to_string(self):
        string_preprocessor = StringPreprocessor()
        self.assertEquals('123', string_preprocessor.process('123'))