import json
import time
from typing import Any, Callable, Dict

import tiktoken

from prompt_optimizer.wrapper.base import Wrapper


class OpenAIWrapper(Wrapper):
    """
    Wrapper class for OpenAI API.

    Inherits from the base Wrapper class.

    Attributes:
        db_manager: The database manager object.
        poptimizer: The poptimizer object.
    """

    def __init__(self, db_manager, poptimizer):
        """
        Initializes a new instance of the OpenAIWrapper class.

        Args:
            db_manager: The database manager object.
            poptimizer: The poptimizer object.
        """
        super().__init__(db_manager, poptimizer)

    def num_tokens_from_messages(self, messages, model="gpt-3.5-turbo-0301"):
        """
        Source: https://stackoverflow.com/a/76044069
        https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
        Returns the number of tokens used by a list of messages."""
        pass

    def wrap(self, openai_func: Callable[..., Any], *args, **kwargs) -> Dict[str, Any]:
        """
        Wraps the OpenAI function with additional functionality.

        Args:
            openai_func: The OpenAI function to be wrapped.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The response from the OpenAI function.

        Raises:
            KeyError: If the 'model' or 'messages' key is missing in kwargs.
        """
        pass

    def __call__(self, *args, **kwargs) -> Dict[str, Any]:
        """
        Calls the OpenAIWrapper instance as a function.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The response from the OpenAI function.
        """
        return self.wrap(*args, **kwargs)
