class TextProcessor:

    def __init__(self):
        """ Baseline text processor"""

    def process(self, text):
        """ Input: List of words [w1,w2,w3,....]"""
        """ Output: List of token (allows to split words into parts: """
        """ remove ,;# etc from words """
        for t in text:
            templist = []
            for word in t:
                if word[0] == '#':
                    word = word[1:]
                    templist.append(word)
                elif word[0:4] == 'http':
                    word = word[0]
                else:
                    templist.append(word)
            t = templist
        

        return text
