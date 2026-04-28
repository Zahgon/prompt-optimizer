import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

from prompt_optimizer.metric.base import Metric


class BERTScoreMetric(Metric):
    """
    BERTScoreMetric is a metric that calculates precision, recall, and F1 score based on BERT embeddings.
    It inherits from the Metric base class.

    Example:
        >>> from prompt_optimizer.metric import BERTScoreMetric
        >>> metric = BERTScoreMetric()
        >>> res = metric("default prompt...", "optimized prompt...")
    """

    def __init__(self):
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "bert-base-uncased", num_labels=2
        )

    def run(self, prompt_before: str, prompt_after: str) -> dict:
        """
        Calculates precision, recall, and F1 score based on BERT embeddings.

        Args:
            prompt_before (str): The text before the prompt.
            prompt_after (str): The text after the prompt.

        Returns:
            dict: A dictionary containing the precision, recall, and F1 score.
        """
        pass
