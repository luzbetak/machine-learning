from collections import Counter
from nltk import pos_tag
from nltk import pos_tag, word_tokenize
from nltk.tokenize import word_tokenize
import time

# ----------------------------- GLOBAL VARIABLES ----------------------------- #
debug             = False
pause             = 1
noun_significance = 0
noun_run_length   = 0
text_length       = 0

# ----------------------------------------------------------------------------- #
def compute_noun_run_length(text):

    global noun_run_length

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    max_run_length = 0
    current_run_length = 0
    for word, tag in tagged:
        if tag.startswith('NN'):
            current_run_length += 1
            max_run_length = max(current_run_length, max_run_length)
        else:
            current_run_length = 0

    noun_run_length = max_run_length



def compute_noun_significance(text):

    global noun_significance

    # Tokenize the text
    tokens = word_tokenize(text)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(tokens)

    # Count the occurrences of each part of speech
    pos_counts = Counter(tag for word, tag in pos_tags)

    # Get the total number of words
    total_words = sum(pos_counts.values())

    # Get the total number of nouns (NN, NNP, NNS, NNPS are the POS tags for nouns)
    total_nouns = sum(pos_counts[tag] for tag in ['NN', 'NNS', 'NNP', 'NNPS'])

    # Compute the percentage of words that are nouns
    noun_significance = (total_nouns / total_words) * 100

    return noun_significance


def lingua_tagger_statistics(description):
    global noun_significance, noun_run_length, text_length

    text_length = len(description)
    compute_noun_run_length(description)
    compute_noun_significance(description)

    print(f"Description Length : {text_length}")
    print(f"Noun Significance  : {noun_significance}")
    print(f"Noun Run_length    : {noun_run_length}")

if __name__ == "__main__":

    text = """
Part-of-Speech Tagging, often abbreviated as POS Tagging, is a common task in 
Natural Language Processing (NLP) where each word in a sentence is labeled with its appropriate part of speech. 
This could include labels such as noun, verb, adjective, adverb, pronoun, preposition, conjunction, interjection, 
and sometimes more detailed categories like plural noun, past-tense verb, etc.
    """

    lingua_tagger_statistics(text)

