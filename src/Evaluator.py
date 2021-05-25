import math


class Evaluator:

    def __init__(self, lm, thresh):
        self.lm = lm
        self.thresh = thresh

    def eval(self, text, target):

        tn = 0
        tp = 0
        fp = 0
        fn = 0

        for i in range(len(text)):
            # print("Checking", text[i], "with reference:", target[i])
            # print(text[i])
            prob = self.lm.calcProb((text[i]))
            # print(prob);
            if prob >= self.thresh:
                if target[i] == '1':
                    tp += 1
                    # print("True positive")
                else:
                    fp += 1
                    # print("False positive")
            else:
                if target[i] == '1':
                    fn += 1
                    # print("False negative")
                else:
                    tn += 1
                    # print("True negative")

        print("True negativ:", tn)
        print("True positiv:", tp)
        print("False negativ:", fn)
        print("False positiv", fp)
        precision = 1.0 * tp / (tp + fp)
        recall = 1.0 * tp / (tp + fn)
        fs = precision * recall / (precision + recall)
        print("Precision:", precision)
        print("Recall:", recall)
        print("Fscore:", fs)
