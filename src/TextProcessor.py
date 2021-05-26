import re


class TextProcessor:

    def __init__(self):
        """ Baseline text processor"""

    def process(self, text):
        """ text = list of tweets, where very tweet in turn is a list of words"""
        """ Method removes symbols and links (links are t.co links, no information)"""

        new_text = []
        for tweet in text:
            new_tweet = []
            for word in tweet:
                new_word = re.sub("[!@#$,.?=:-]", "", word)
                if new_word[0:4] == "http":
                    new_word = ""
                if len(new_word) > 0:
                    new_tweet.append(new_word)
            new_text.append(new_tweet)

        return new_text
