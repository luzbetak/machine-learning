Natural Language Processing (NLP)
=================================


Natural Language Processing, often abbreviated as NLP, is a branch of artificial intelligence (AI) that deals with the interaction between computers and humans using natural language. The ultimate objective of NLP is to read, decipher, understand, and make sense of human language in a valuable way.

Key tasks in NLP include:

- **Sentiment Analysis:** Understanding the sentiment or opinion of a given text.
- **Machine Translation:** Translating text from one language to another.
- **Named Entity Recognition (NER):** Identifying the entities in the text (like a person, organization, date, etc.)
- **Speech Recognition:** Converting spoken language into written form.
- **Text Summarization:** Automatically generating a condensed version of a larger text.
- **Topic Modeling:** Identifying the main themes in a document or set of documents.

Modern NLP applications include chatbots, translation apps, sentiment analysis tools, voice assistants, and more. Libraries like NLTK, SpaCy, and transformers (Hugging Face) provide tools and resources to build NLP applications.


---
Part-of-Speech Tagger
=====================

| POS | Description | Example |
| --- | ----------- | ------- |
| **ADJ** | adjective | new, good, high, special, big, local |
| **ADV** | adverb | really, already, still, early, now |
| **CNJ** | conjunction | and, or, but, if, while, although |
| **DET** | determiner | the, a, some, most, every, no |
| **EX** | existential | there, there's |
| **FW** | foreign word | dolce, ersatz, esprit, quo, maitre |
| **MOD** | modal verb | will, can, would, may, must, should |
| **N** | noun | year, home, costs, time, education |
| **NP** | proper noun | Alison, Africa, April, Washington |
| **NUM** | number | twenty-four, fourth, 1991, 14:21 |
| **PRO** | pronoun | he, their, her, its, my, I, us |
| **P** | preposition | on, of, at, with, by, into, under |
| **TO** | the word to | to |
| **UH** | interjection | ah, bang, ha, whee, hmf, oops |
| **V** | verb | is, has, get, do, make, see, run |
| **VD** | past tense | said, took, get, do, make, asked |
| **VG** | present participle | making, going, playing, working |
| **VN** | past participle | given, taken, begun, sung |
| **WH** | wh determiner | who, which, when, what, where, how |

## Part-of-Speech Tagging (POS Tagging)

Part-of-Speech Tagging, often abbreviated as POS Tagging, is a common task in Natural Language Processing (NLP) where each word in a sentence is labeled with its appropriate part of speech. This could include labels such as noun, verb, adjective, adverb, pronoun, preposition, conjunction, interjection, and sometimes more detailed categories like plural noun, past-tense verb, etc.

Here's an example of POS tagging:

- Sentence: "Apple is looking at buying U.K. startup for $1 billion"
- POS Tags: "Apple (NOUN) is (VERB) looking (VERB) at (ADP) buying (VERB) U.K. (PROPN) startup (NOUN) for (ADP) $1 billion (MONEY)"

POS tagging is useful for various NLP tasks such as Named Entity Recognition (NER), parsing, question answering, and machine translation. It helps the algorithm to understand the context of the sentence and the role of each word in the sentence.

Modern NLP libraries like NLTK, SpaCy, and StanfordNLP have pre-trained POS taggers available for use.


---

| **Abbreviation** | **Description** | **Example** |
| :---: | :--- | :--- |
| **CC** | Conjunction, coordinating | and, or |
| **CD** | Adjective, cardinal number | 3, fifteen |
| **DET** | Determiner | this, each, some |
| **EX** | Pronoun, existential there | there |
| **FW** | Foreign words | |
| **IN** | Preposition / Conjunction | for, of, although, that |
| **JJ** | Adjective | happy, bad |
| **JJR** | Adjective, comparative | happier, worse |
| **JJS** | Adjective, superlative | happiest, worst |
| **LS** | Symbol, list item | A, A. |
| **MD** | Verb, modal | can, could, 'll |
| **NN** | Noun | aircraft, data |
| **NNP** | Noun, proper | London, Michael |
| **NNPS** | Noun, proper, plural | Australians, Methodists |
| **NNS** | Noun, plural | women, books |
| **PDT** | Determiner, prequalifier | quite, all, half |
| **POS** | Possessive | 's, ' |
| **PRP** | Determiner, possessive second | mine, yours |
| **PRPS** | Determiner, possessive | their, your |
| **RB** | Adverb | often, not, very, here |
| **RBR** | Adverb, comparative | faster |
| **RBS** | Adverb, superlative | fastest |
| **RP** | Adverb, particle | up, off, out |
| **SYM** | Symbol | * |
| **TO** | Preposition | to |
| **UH** | Interjection | oh, yes, mmm |
| **VB** | Verb, infinitive | take, live |
| **VBD** | Verb, past tense | took, lived |
| **VBG** | Verb, gerund | taking, living |
| **VBN** | Verb, past/passive participle | taken, lived |
| **VBP** | Verb, base present form | take, live |
| **VBZ** | Verb, present 3SG -s form | takes, lives |
| **WDT** | Determiner, question | which, whatever |
| **WP** | Pronoun, question | who, whoever |
| **WPS** | Determiner, possessive & question | whose |
| **WRB** | Adverb, question | when, how, however |
| **PP** | Punctuation, sentence ender | ., !, ? |
| **PPC** | Punctuation, comma | , |
| **PPD** | Punctuation, dollar sign | $ |
| **PPL** | Punctuation, quotation mark left | `` |
| **PPR** | Punctuation, quotation mark right | '' |
| **PPS** | Punctuation, colon, semicolon, elipsis | :, ..., - |
| **LRB** | Punctuation, left bracket | (, {, [ |
| **RRB** | Punctuation, right bracket | ), }, ] |


---

## Reference: 
http://www.nltk.org/
