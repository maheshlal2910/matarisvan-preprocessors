import nltk

class TextExtractor(object):
    
    def process(self, html):
        cleaned_text = nltk.clean_html(html)
        return cleaned_text.strip()


class StringPreprocessor(object):
    
    def process(self, value):
        str_val = str(value)
        return str_val
        