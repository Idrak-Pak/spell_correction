from SpellCheckerInterface import SpellCheckerInterface
from spellchecker import SpellChecker


class PySpellChecker(SpellCheckerInterface):
    """
    Implementation of SpellCheckerInterface using the spellchecker library.
    """

    def __init__(self, dict_path=''):
        """
        Initialize the PySpellChecker object.

        Args:
            dict_path (str): The path to the dictionary file.
        """
        self.dict_path = dict_path
        self.spell = SpellChecker(language=None, case_sensitive=True)
        self.spell.word_frequency.load_text_file(self.dict_path)

    def correct(self, text):
        """
        Correct the given text.

        Args:
            text (str): The text to be corrected.

        Returns:
            str: The corrected text.
        """
        misspelled = self.spell.unknown([text])
        for word in misspelled:
            corrected_word = self.spell.correction(word)
            return corrected_word
