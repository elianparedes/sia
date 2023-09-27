from src.classes.metrics.MetricABC import MetricABC


class Recall(MetricABC):

    @classmethod
    def calculate(cls, true_positive, true_negative, false_positive, false_negative):
        return true_positive / (true_positive + false_negative)
