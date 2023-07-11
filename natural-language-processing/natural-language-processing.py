import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk
from nltk.chunk import conlltags2tree, tree2conlltags

# Download necessary NLTK data
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

# Process whole documents
text = ("When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

# Tokenize and apply part-of-speech tagging
doc = nltk.pos_tag(word_tokenize(text))

# Extract named entities
ne_tree = ne_chunk(doc)
named_entities = []
for t in ne_tree.subtrees():
    if t.label() == 'NE':
        named_entities.append(list(t))  # Named Entity

print("Named entities:", named_entities)

# Extract noun phrases using a shallow parser
grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = nltk.RegexpParser(grammar)
tree = cp.parse(doc)

# Extracting noun phrases
noun_phrases = []
for subtree in tree.subtrees():
    if subtree.label() == 'NP':
        noun_phrases.append(subtree)

print("Noun phrases:", noun_phrases)

# Extract verbs
verbs = [word for word, pos in doc if pos.startswith('VB')]

print("Verbs:", verbs)


"""
OUTPUT:

[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /Users/kevin/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package maxent_ne_chunker to
[nltk_data]     /Users/kevin/nltk_data...
[nltk_data]   Package maxent_ne_chunker is already up-to-date!
[nltk_data] Downloading package words to /Users/kevin/nltk_data...
[nltk_data]   Package words is already up-to-date!
[nltk_data] Downloading package punkt to /Users/kevin/nltk_data...
[nltk_data]   Package punkt is already up-to-date!


Named entities: []
Noun phrases: [
                  Tree('NP', [('the', 'DT'), ('company', 'NN')])
                , Tree('NP', [('major', 'JJ'), ('American', 'JJ'), ('car', 'NN')])
                , Tree('NP', [('hand', 'NN')])
                , Tree('NP', [('’', 'JJ'), ('t', 'NN')])
                , Tree('NP', [('worth', 'NN')])
                , Tree('NP', [('an', 'DT'), ('interview', 'NN')])
                , Tree('NP', [('this', 'DT'), ('week', 'NN')])
             ]

Verbs: ['started', 'working', 'took', '“', 'tell', 'shake', 'turn', 'wasn', 'talking', 'said']
"""

