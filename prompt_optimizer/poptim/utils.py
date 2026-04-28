from typing import Any, Callable, List, Tuple


class DotDict(dict):
    """
    DotDict is a subclass of the built-in dict class that allows accessing dictionary keys using dot notation.
    It provides the ability to get and set attributes as if they were dictionary keys.

    Example:
        d = DotDict()
        d['key'] = 'value'
        print(d.key)  # Output: 'value'
    """

    def __getattr__(self, attr: str) -> Any:
        """
        Get the value associated with the given attribute.

        Args:
            attr (str): The attribute name.

        Returns:
            Any: The value associated with the attribute.

        Raises:
            AttributeError: If the attribute does not exist in the dictionary.
        """
        if attr in self:
            return self[attr]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{attr}'"
        )

    def __setattr__(self, attr: str, value: Any) -> None:
        """
        Set the value associated with the given attribute.

        Args:
            attr (str): The attribute name.
            value (Any): The value to be associated with the attribute.

        Returns:
            None
        """
        self[attr] = value


class ParseError(Exception):
    """
    ParseError is a custom exception class raised when a parsing error occurs.
    It inherits from the built-in Exception class.

    Attributes:
        message (str): The error message describing the parsing error.
        prompt (str): The prompt where the parsing error occurred.
    """

    def __init__(self, message: str, prompt: str) -> None:
        """
        Initialize a new ParseError instance.

        Args:
            message (str): The error message describing the parsing error.
            prompt (str): The prompt where the parsing error occurred.

        Returns:
            None
        """
        super().__init__(message)
        self.prompt = prompt

    def __str__(self) -> str:
        """
        Return a string representation of the ParseError instance.

        Returns:
            str: A formatted string representing the ParseError instance.
                 Example: "ParseError: <message> in `Prompt`: <prompt>"
        """
        return f"ParseError: {self.args[0]} in `Prompt`: {self.prompt}"


def parse_protect_tags(prompt: str, protect_tag: str) -> Tuple[List[str], List[str]]:
    """
    Parse the given prompt and extract protected chunks enclosed by protect tags.

    Args:
        prompt (str): The prompt string to parse.
        protect_tag (str): The protect tag used to enclose the protected chunks.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists.
            - The first list contains the chunks of the prompt that are not protected.
            - The second list contains the protected chunks extracted from the prompt.

    Raises:
        ParseError: If there are nested protect tags, an unclosed protect tag, or invalid protect tag sequences.
    """
    pass


def protected_runner(run: Callable) -> Callable:
    """
    Decorator function that runs the provided 'run' function in chunks for a given object and prompt.
    It extracts protected chunks from the prompt and runs the 'run' function on each non-protected chunk.

    Args:
        run (Callable): The function to run on each non-protected chunk.

    Returns:
        Callable: A wrapper function that performs the chunked execution of the 'run' function.

    Example:
        @protected_runner
        def my_run_function(obj, prompt, *args, **kwargs):
            # Perform some operations on prompt
            return optimized_prompt

        # Usage
        optimized_result = my_run_function(my_obj, my_prompt, my_args, my_kwargs)
    """
    pass
