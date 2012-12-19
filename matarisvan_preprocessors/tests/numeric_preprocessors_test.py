import unittest

from matarisvan_preprocessors.numeric_preprocessors import LongPreprocessor

class LongPreprocessorTest(unittest.TestCase):
    
    def test_should_convert_string_to_long(self):
        long_preprocessor = LongPreprocessor()
        self.assertEquals(123, long_preprocessor.process('123'))
    
    def test_should_convert_int_to_long(self):
        long_preprocessor = LongPreprocessor()
        self.assertEquals(123, long_preprocessor.process(123))       