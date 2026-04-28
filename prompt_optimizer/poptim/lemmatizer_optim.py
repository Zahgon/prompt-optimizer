import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

from prompt_optimizer.poptim.base import PromptOptim


class LemmatizerOptim(PromptOptim):
    """
    LemmatizerOptim is a prompt optimization technique based on lemmatization.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import LemmatizerOptim
        >>> p_optimizer = LemmatizerOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the LemmatizerOptim.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)
        self.lemmatizer = WordNetLemmatizer()
        nltk.download("averaged_perceptron_tagger")
        nltk.download("wordnet")

    def get_wordnet_pos(self, word: str) -> str:
        """
        Maps the POS tag from NLTK to WordNet POS tags.

        Args:
            word (str): The word to determine the POS tag.

        Returns:
            str: The WordNet POS tag.
        """
        pass

    def optimize(self, prompt: str) -> str:
        """
        Runs the lemmatizer prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        pass
