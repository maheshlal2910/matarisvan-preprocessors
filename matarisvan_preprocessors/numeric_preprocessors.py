class LongPreprocessor(object):
    
    def process(self, value):
        long_val = long(value)
        return long_val


class StringPreprocessor(object):
    
    def process(self, value):
        str_val = str(value)
        return str_val