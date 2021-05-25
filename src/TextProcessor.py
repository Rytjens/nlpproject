import re

class TextProcessor:

    def __init__(self):
        """ Baseline text processor"""

    def process(self, text):
        """ text = list of tweets, where very tweet in turn is a list of words"""
        """ Method removes symbols and links (links are t.co links, no information)"""

        newText = []
        for tweet in text:
            newTweet = []
            for word in tweet:
                newWord = re.sub('[!@#$,.?=-:]', '', word)
                if (newWord[0:4] == 'http'):
                    newWord = ''
                if (len(newWord) > 0):
                    newTweet.append(newWord)
            newText.append(newTweet)
         

        return newText
