import re
import unicodedata
import nltk


class TextsPreprocessor:

    def __init__(self, keyword):
        self.keyword = keyword

    def normalizeText(self, text):
        text = unicodedata.normalize('NFKC', text)
        return text

    def deleteURLs(self, text):
        text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)
        return text

    def deleteSymbols(self, text):
        text = re.sub(r'[\(\)\[\]’\']', ' ', text)
        text = re.sub(r'[!?\";:\-_/\-]', '', text)
        return text

    def deletePeriods(self, text):
        text = re.sub(r'\.+', '.', text)
        return text

    def deleteNumwords(self, text):
        text = re.sub(r'\S*\d+\S*', '', text)
        return text

    def exprText(self, text):
        text = self.normalizeText(text)
        text = self.deleteURLs(text)
        text = self.deleteSymbols(text)
        text = self.deletePeriods(text)
        text = self.deleteNumwords(text)
        text = text.strip()
        return text

    def extractWords(self, text):
        words = text.split()
        return words

    def readStopwords(self):
        with open('stopwords.txt', 'r') as f:
            stopwords = f.read().splitlines()
        return stopwords

    def eliminateStopwords(self, words):
        newWords = list()
        stopwords = self.readStopwords()
        for word in words:
            if word not in stopwords:
                newWords.append(word)
        return newWords

    def lemmatizeWords(self, words):
        lemmatizer = nltk.WordNetLemmatizer()
        words = [lemmatizer.lemmatize(word, pos='v') for word in words]
        words = [lemmatizer.lemmatize(word, pos='n') for word in words]
        return words

    def putPeriods(self, text):
        text = re.sub(r'(\r\n|\n|\r)', '.', text)
        text = re.sub(r'\.{2,}', '.', text)
        return text

    def deleteExtraSpaces(self, text):
        text = re.sub(r'\s{2,}', ' ', text)
        return text

    def stemWords(self, words):
        stemmer = nltk.PorterStemmer()
        newWords = [stemmer.stem(word) for word in words]
        return newWords

    def eliminateKeyword(self, words):
        newWords = [word for word in words if word != self.keyword]
        return newWords

    def makePlainText(self, words):
        text = ' '.join(words)
        return text

    def replaceENDSymbol(self, text):
        text = re.sub(r'<end>', '.', text)
        return text

    def preprocess(self, texts):
        texts = list(map((lambda x: x.lower()), texts))
        text = '.'.join(texts)
        text = self.exprText(text)
        words = self.extractWords(text)
        # words = self.eliminateStopwords(words)
        words = self.lemmatizeWords(words)
        # words = self.stemWords(words)
        # words = self.eliminateKeyword(words)
        text = self.makePlainText(words)
        text = self.putPeriods(text)
        text = self.deleteExtraSpaces(text)
        # text = self.replaceENDSymbol(text)
        return text
