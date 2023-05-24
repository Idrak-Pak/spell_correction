# Idrak Spell Correction Module

This module correct the spelling from the given Vocab. Y
## Requirements:

```
pip install -r requirments.txt
```

## Ussage: 

1. Add a txt file as vocab. Check food_vocab.txt as example
2. Add `config['corrector']['dict_path']= 'food_vocab.txt' ` as a path to vocab
3. To run the code 

```
    from Corrector import Corrector
    from spellcheck_config import config
    word_corrector = Corrector(**config)
    print(word_corrector.corrector.correct('kher'))
```
