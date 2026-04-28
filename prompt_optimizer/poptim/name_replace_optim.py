import nltk

from prompt_optimizer.poptim.base import PromptOptim


class NameReplaceOptim(PromptOptim):
    """
    NameReplaceOptim is a prompt optimization technique based on replacing names in the prompt.
    Some names have lower token count (1) than others. Higher token count names can be replaced by
    such names to reduce token complexity. `self.opti_names` contains the pre-made list of such names
    for `tiktokenizer`. The list will need to be modified for other tokenizers.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import NameReplaceOptim
        >>> p_optimizer = NameReplaceOptim()
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, verbose: bool = False, metrics: list = []):
        """
        Initializes the NameReplaceOptim.

        Args:
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)
        self.opti_names = self.get_opti_names()

    def download(self):
        """
        Downloads the required NLTK resources.
        """
        pass

    def process(self, text: str) -> nltk.Tree:
        """
        Processes the text using NLTK to identify named entities.

        Args:
            text (str): The text to process.

        Returns:
            nltk.Tree: The parsed sentence tree containing named entities.
        """
        pass

    def get_opti_names(self) -> list:
        """
        Retrieves the list of optimized names.

        Returns:
            list: The list of optimized names.
        """
        pass

    def gen_name_map(self, text: str) -> dict:
        """
        Generates a mapping of names in the prompt to optimized names.

        Args:
            text (str): The prompt text.

        Returns:
            dict: The mapping of names to optimized names.
        """
        pass

    def opti_name_replace(self, text: str, mapping: dict) -> str:
        """
        Replaces names in the text with optimized names based on the mapping.

        Args:
            text (str): The text to perform name replacement.
            mapping (dict): The mapping of names to optimized names.

        Returns:
            str: The text with replaced names.
        """
        pass

    def optimize(self, prompt: str) -> str:
        """
        Runs the prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        pass
