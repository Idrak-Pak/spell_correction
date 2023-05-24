from PySpellChecker import PySpellChecker
from spellcheck_config import config


class Corrector:
    """
    Corrector class for performing spell-checking using different corrector types.
    """

    def __init__(self, **kwargs):
        """
        Initialize the Corrector object.

        Args:
            **kwargs: Additional keyword arguments.
                - corrector_type (str): The type of corrector to use.
                - corrector (dict): Configuration options for the corrector.
        """
        self.corrector = self.get_corrector(kwargs['corrector_type'], **kwargs['corrector'])

    def get_corrector(self, corrector_type, **kwargs):
        """
        Get the corrector instance based on the corrector type.

        Args:
            corrector_type (str): The type of corrector.
            **kwargs: Additional keyword arguments for the corrector.

        Returns:
            object: The corrector instance.

        Raises:
            ValueError: If the corrector type is unknown.
        """
        if corrector_type == 'pyspellchecker':
            return PySpellChecker(**kwargs)
        else:
            raise ValueError('Unknown corrector type.')

            
if __name__ == "__main__":
    # Example usage
    word_corrector = Corrector(**config)
    print(word_corrector.corrector.correct('BB-Styke'))
