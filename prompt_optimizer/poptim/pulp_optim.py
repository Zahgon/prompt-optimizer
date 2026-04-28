from pulp import LpBinary, LpMinimize, LpProblem, LpVariable, lpSum

from prompt_optimizer.poptim.base import PromptOptim


class PulpOptim(PromptOptim):
    """
    PulpOptim is a prompt optimization technique based on integer linear programming using the Pulp library.

    It inherits from the PromptOptim base class.

    Example:
        >>> from prompt_optimizer.poptim import PulpOptim
        >>> p_optimizer = PulpOptim(p=0.1)
        >>> res = p_optimizer("example prompt...")
        >>> optimized_prompt = res.content
    """

    def __init__(self, p: float = 0.1, verbose: bool = False, metrics: list = []):
        """
        Initializes the PulpOptim.

        Args:
            p (float, optional): The aggression factor controlling the reduction in the number of tokens. Defaults to 0.1. Higher `p` corresponds to lower token output count.
            verbose (bool, optional): Flag indicating whether to enable verbose output. Defaults to False.
            metrics (list, optional): A list of metric names to evaluate during optimization. Defaults to an empty list.
        """
        super().__init__(verbose, metrics)
        self.aggression = p  # will reduce num tokens by aggression*100%

    def optimize(self, prompt: str) -> str:
        """
        Runs the prompt optimization technique on the prompt.

        Args:
            prompt (str): The prompt text.

        Returns:
            str: The optimized prompt text.
        """
        pass
