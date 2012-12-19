import unittest

from matarisvan_preprocessors.text_preprocessors import TextExtractor

class TextExtractorTest(unittest.TestCase):
    
    def test_should_get_text_from_html(self):
        text_extractor = TextExtractor()
        html = """<html> <body> hello world </body> </html>"""
        text = """hello world"""
        self.assertEquals(text.replace('\n', ''), text_extractor.process(html))