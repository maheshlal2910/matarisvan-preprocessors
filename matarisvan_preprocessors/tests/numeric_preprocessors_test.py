import unittest

from matarisvan_preprocessors.numeric_preprocessors import LongPreprocessor, StringPreprocessor

class LongPreprocessorTest(unittest.TestCase):
    
    def test_should_convert_string_to_long(self):
        long_preprocessor = LongPreprocessor()
        self.assertEquals(123, long_preprocessor.process('123'))
    
    def test_should_convert_int_to_long(self):
        long_preprocessor = LongPreprocessor()
        self.assertEquals(123, long_preprocessor.process(123))

class StringPreprocessorTest(unittest.TestCase):
    
    def test_should_convert_numeric_to_string(self):
        string_preprocessor = StringPreprocessor()
        self.assertEquals('123', string_preprocessor.process(123))
    
    def test_should_convert_string_to_string(self):
        string_preprocessor = StringPreprocessor()
        self.assertEquals('123', string_preprocessor.process('123'))        