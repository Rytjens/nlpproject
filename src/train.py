#!/usr/bin/python

import argparse
import pandas

from Evaluator import Evaluator
from LanguageModel import LanguageModel
from TextProcessor import TextProcessor


def main():
    parser = argparse.ArgumentParser(description='Script to train a language model')
    parser.add_argument("--train", default="../data/train.csv", type=str,
                        help="text file containing the training data")
    parser.add_argument("--test", default="../data/test.csv", type=str,
                        help="text file containing the test data")

    args = parser.parse_args()

    """ Init language model and text processor"""
    lm = LanguageModel()
    processor = TextProcessor()
    eval = Evaluator(lm, .5)

    """ Load training data and process text by the Text Processor"""
    text, target = getTextandTarget(args.train)
    prepro = processor.process(text)

    """ Split text into training and test data """
    train_data = []
    train_target = []
    test_data = []
    test_target = []

    """ Every fourth tweet gets added to the test set """
    for i in range(len(prepro)):
        if i % 4 == 0:
            test_data.append(prepro[i])
            test_target.append(target[i])
        else:
            train_data.append(prepro[i])
            train_target.append(target[i])

    print("Train language model ....")
    lm.train(train_data, train_target)
    print("Language model trained")

    print("Test data")
    eval.eval(test_data, test_target)


def getTextandTarget(filename):
    colnames = ['id', 'keyword', 'location', 'text', 'target']
    data = pandas.read_csv(filename, names=colnames)

    text = [l.strip().split() for l in data['text'].tolist()]
    text = [sublist for sublist in text]
    return text, data['target']


if __name__ == "__main__":
    main()
