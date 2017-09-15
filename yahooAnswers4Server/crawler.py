import requests
from bs4 import BeautifulSoup
from abc import ABCMeta, abstractmethod
import random
import time
from tqdm import tqdm


class Processor(metaclass=ABCMeta):
    _baseSearchURL = ''


class Processor4YA(Processor):
    _baseSearchURL = 'https://answers.search.yahoo.com/search?fr=uh3_answers_vert_gs&p='

    def crawl(self, keyword, times):
        searchPagesCrawler = SearchPagesCrawler()
        answerPageURLs = searchPagesCrawler.crawl(
            self._baseSearchURL + keyword, times=times)
        answerPagesCrawler = AnswerPagesCrawler()
        questions, answers = answerPagesCrawler.crawl(answerPageURLs)
        return questions, answers


class Crawler(metaclass=ABCMeta):

    def getPage(self, targetURL):
        page = requests.get(targetURL)
        text = page.text
        return text

    def soupPage(self, text):
        soup = BeautifulSoup(text, 'lxml')
        return soup

    def getSoupPage(self, targetPageURL):
        text = self.getPage(targetPageURL)
        soup = self.soupPage(text)
        return soup

    @abstractmethod
    def analyzePage(self):
        pass

    @abstractmethod
    def crawl(self):
        pass


class SearchPagesCrawler(Crawler):

    def getAnswerURLs(self, soup):
        answerURLs = soup.find_all('a', class_='lh-17')
        answerURLs = list(map((lambda x: x['href']), answerURLs))
        return answerURLs

    def getNextURL(self, soup):
        nextURL = soup.find('a', class_='next')['href']
        return nextURL

    def analyzePage(self, soupPage):
        answerPageURLs = self.getAnswerURLs(soupPage)
        nextPageURL = self.getNextURL(soupPage)
        return [answerPageURLs, nextPageURL]

    def crawl(self, targetPageURL, times):
        answerPageURLs = list()
        for i in tqdm(range(times)):
            time.sleep(random.randint(3, 5))
            soupPage = self.getSoupPage(targetPageURL)
            URLs = self.analyzePage(soupPage)
            answerPageURLs.extend(URLs[0])
            targetPageURL = URLs[1]
        return answerPageURLs


class AnswerPagesCrawler(Crawler):

    def getQuestion(self, soup):
        title = soup.find('h1', class_='Fz-24').get_text()
        question = soup.find('span', class_='ya-q-text').get_text()
        return [title, question]

    def getAnswers(self, soup):
        answers = soup.find_all('span', class_='ya-q-full-text')
        answers = list(map((lambda x: x.get_text()), answers))
        return answers

    def analyzePage(self, soupPage):
        question = self.getQuestion(soupPage)
        answers = self.getAnswers(soupPage)
        return question, answers

    def crawl(self, urls):
        allQuestions = list()
        allAnswers = list()
        for url in tqdm(urls):
            time.sleep(random.randint(3, 5))
            soupPage = self.getSoupPage(url)
            question, answers = self.analyzePage(soupPage)
            allQuestions.extend(question)
            allAnswers.extend(answers)
        return allQuestions, allAnswers
