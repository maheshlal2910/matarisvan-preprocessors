import nltk

class TextExtractor(object):
    
    def process(self, html):
        cleaned_text = nltk.clean_html(html)
        return cleaned_text.strip()