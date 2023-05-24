config = dict()

# -------------- General configs ------------#
config["words"] = 1
config['corrector_type'] = 'pyspellchecker'

#-------- py spell checker config -----------#

if config['corrector_type'] == 'pyspellchecker':
    config['corrector'] = dict()
    config['corrector']['dict_path'] =  'food_vocab.txt'
