from SpellCheckerInterface import SpellCheckerInterface
from spellchecker import SpellChecker
from fuzzywuzzy import process
import pandas as pd

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
        print(self.dict_path)
        self.spell = SpellChecker(language=None, case_sensitive=True)
        self.spell.word_frequency.load_text_file(self.dict_path)
        
        df = pd.read_csv(self.dict_path, delimiter='\t',header=None)  # Use '\t' as the delimiter for tab-separated files

        self.vocab_list = df.iloc[:, 0]
        first_column = df.iloc[:, 0]
        self.custom_corrections = {
                'suffering': 'supereme',
                'B-stick' : 'beef steaks',
                # Add more custom corrections here as needed
            }
        

    def correct(self, text):
        """
        Correct the given text.

        Args:
            text (str): The text to be corrected.

        Returns:
            str: The corrected text.
        """
        # If a known word (word present in dictionary)
        if self.spell.known([text]):
            return text
        
        corrected_word = None
        misspelled = self.spell.unknown([text])
        

        for word in misspelled:
            if word in self.custom_corrections:
                # If the word is in the custom corrections dictionary, use that correction
                corrected_word = self.custom_corrections[word]
            else:
                corrected_word = self.spell.correction(word)
                # If neighter word directly matched with both dictionaries 
                # Get the closest possible
                if not corrected_word and 'food' in self.dict_path:
                    best_match = process.extractOne(text, self.custom_corrections.keys())
                    corrected_word = self.custom_corrections[best_match[0]]
                else: 
                    # looking from address list using fuzzywuzzy
                    best_matches  = process.extractBests(text,self.vocab_list)
                    corrected_word=None
                    for i in best_matches:
                        if i[0][0] == text[0]: #if first character matched
                            corrected_word=i[0]
                            break
                    
                if not corrected_word:
                    print('All Method Could Not find Correct word')
                    corrected_word = ''
            return corrected_word
