import re

class TextProcessor:

    def __init__(self):
        """ Baseline text processor"""

    def process(self, text):
        """ Input: List of words [w1,w2,w3,....]"""
        """ Output: List of token (allows to split words into parts: """
        """ remove ,;# etc from words """

        """ text = [word.replace('#', '') for t in text for word in t] """

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
