from abc import ABC

from src.classes.metrics.MetricABC import MetricABC


class Accuracy(MetricABC):

    @classmethod
    def calculate(cls, true_positive, true_negative, false_positive, false_negative):
        return (true_positive + true_negative) / (true_positive + true_negative + false_positive + false_negative)
