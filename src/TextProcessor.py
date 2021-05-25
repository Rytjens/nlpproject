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
                    word = word.replace(word[0:2], word[1:2])
                    templist.append(word)
                    print(word)
                elif word[0:4] == 'http':
                    word = word
                else:
                    templist.append(word)
            t = templist
 

        return text
