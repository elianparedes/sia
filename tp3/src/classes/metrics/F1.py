from src.classes.metrics.MetricABC import MetricABC
from src.classes.metrics.Precision import Precision
from src.classes.metrics.Recall import Recall


class F1(MetricABC):

    @classmethod
    def calculate(cls, true_positive, true_negative, false_positive, false_negative):
        precision_value = Precision.calculate(true_positive, true_negative, false_positive, false_negative)
        recall_value = Recall.calculate(true_positive, true_negative, false_positive, false_negative)
        return (2*precision_value*recall_value)/(precision_value+recall_value)
