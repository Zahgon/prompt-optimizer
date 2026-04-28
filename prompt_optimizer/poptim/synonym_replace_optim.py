import random

import nltk
import tiktoken
from nltk.corpus import wordnet

from prompt_optimizer.poptim.base import PromptOptim


class SynonymReplaceOptim(PromptOptim):
    """
    SynonymReplaceOptim is a prompt optimization technique that replaces words in the prompt with their synonyms.

    Synonyms are words that have similar meanings to the original word. Sometimes a synonym has lower token count
    than the original word.

    Example:
        >>> from prompt_optimizer.poptim import SynonymReplaceOptim
        >>> p_optimizer = SynonymReplaceOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, verbose: bool = False, metrics: list = [], p: float = 0.5):
        """
        Initializes the SynonymReplaceOptim object with the specified parameters.

        Args:
            verbose (bool, optional): If True, print verbose information during optimization. Defaults to False.
            metrics (list, optional): List of metrics to evaluate the optimization. Defaults to [].
            p (float, optional): Probability of replacing a word with a synonym. Defaults to 0.5.
        """
        super().__init__(verbose, metrics)
        self.p = p
        nltk.download("wordnet")
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def get_word_pos(self, word: str) -> str:
        """
        Get the part of speech of a word.

        Args:
            word (str): The word.

        Returns:
            str: The part of speech of the word.
        """
        pass

    def syn_replace(self, word: str) -> str:
        """
        Replace a word with its synonym.

        Args:
            word (str): The word.

        Returns:
            str: The best replacement synonym for the word.
        """
        pass

    def optimize(self, prompt: str) -> str:
        """
        Replaces words in the prompt with their synonyms.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The optimized prompt with replaced synonyms.
        """
        pass
