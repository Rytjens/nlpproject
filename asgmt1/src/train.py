#!/usr/bin/python

import argparse
import pandas


from Evaluator import Evaluator
from LanguageModel import LanguageModel
from TextProcessor import TextProcessor



def main():
    parser = argparse.ArgumentParser(description='Script to train a language model')
    parser.add_argument("--train", default="../../data/train.csv", type=str,
                        help="text file containing the training data")
    parser.add_argument("--test_input", default="../../data/test.csv", type=str,
                        help="text file containing the test data")

    args = parser.parse_args()

    """ Init components """
    """ Use your own langauge model and text processor"""
    processor = TextProcessor()
    lm = LanguageModel(1)
    

    """ Load training data and train language model"""
    text, target = getTextandTarget(args.train)

    """ Process text by the Text Processor"""
    preprocessed = processor.process(text)

    """ Split text into training and test data """
    i = 0
    testData = []
    testTarget = []
    trainData = []
    trainTarget = []
    """ Every fourth tweet gets added to the test set """
    for p in preprocessed:
        if i % 4 == 0:
            testData.append(p)
            testTarget.append(target[i])
        else:
            trainData.append(p)
            trainTarget.append(target[i])
        i += 1

    eval = Evaluator(lm, processor, trainTarget)


    """ Process text by the Text Processor"""
    print("Train language model ....")
    lm.train(trainData, trainTarget)
    print("Language model trained")

    print("Test data")
    test = getText(args.test_input)
    reference = getText(args.test_output)
    prepro_reference = processor.process(reference)
    lm.getPPL(prepro_reference)
    eval.eval(test, reference) 


def getTextandTarget(filename):
    colnames = ['id', 'keyword', 'location', 'text', 'target']
    data = pandas.read_csv(filename, names=colnames)
    

    text = [l.strip().split() for l in data['text'].tolist()]
    text = [sublist for sublist in text]
    return text, data['target']


if __name__ == "__main__":
    main()
