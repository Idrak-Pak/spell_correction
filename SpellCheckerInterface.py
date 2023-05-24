class SpellCheckerInterface:
    """
    Interface for spell checker implementations.
    """

    def __init__(self):
        """
        Initialize the SpellCheckerInterface object.
        """
        pass

    def correct(self, text):
        """
        Correct the given text.

        Args:
            text (str): The text to be corrected.

        Returns:
            str: The corrected text.
        """
        pass
