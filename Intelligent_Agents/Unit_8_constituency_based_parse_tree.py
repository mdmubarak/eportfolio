import nltk
from nltk import Tree

def constituency_parse_tree(sentence):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Part-of-Speech (POS) tagging
    pos_tags = nltk.pos_tag(tokens)

    # Create a chunk grammar to specify the patterns for constituency parsing
    grammar = r"""
        NP: {<DT>?<JJ>*<NN.*>+}      # Noun phrases
        VP: {<VB.*><NP|PP|CLAUSE>*}  # Verb phrases
        PP: {<IN><NP>}               # Prepositional phrases
        CLAUSE: {<NP><VP>}           # Clauses
    """
    cp = nltk.RegexpParser(grammar)

    # Perform constituency parsing
    parse_tree = cp.parse(pos_tags)

    return parse_tree

# Input phrases
phrases = [
    "The government raised interest rates.",
    "The internet gives everyone a voice.",
    "The man saw the dog with the telescope."
]

# Generate parse trees for each phrase
for phrase in phrases:
    tree = constituency_parse_tree(phrase)
    print(phrase)
    tree.pretty_print()
    print("\n")
