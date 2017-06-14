import re
from collections import OrderedDict


SENTENCES = ['MULTI WORD NAME FEATURE_1 FEATURE_2',
             'MULTI WORD NAME FEATURE_3 FEATURE_4',
             'MULTI WORD NAME FEATURE_5 FEATURE_6',
             'MULTI WORD NAME FEATURE_2 FEATURE_6',
             'MULTI WORD NAME FEATURE_3 FEATURE_5',
             'MULTI WORD NAME FEATURE_7 FEATURE_9', ]

def get_words(text):
    """
    Returns words without punctuation
    """
    return re.compile('\w+').findall(text)


def flatten(l):
    """
    Return flatten list when nested (Only one Level!)
    """
    return [item for sublist in l for item in sublist]



def extract_name(labels):
    WORDED_SENTENCES = [get_words(sentence) for sentence in labels]
    JOINED_WORDS = list(OrderedDict.fromkeys(flatten(WORDED_SENTENCES)))

    SETS = [set(sentence) for sentence in WORDED_SENTENCES]
    UNORDERED_WORDS = reduce(lambda x, y: x.intersection(y), SETS, SETS[0])

    RES = []
    for word in UNORDERED_WORDS:
        RES.insert(JOINED_WORDS.index(word), word)
    return ' '.join(RES)

print extract_name(SENTENCES)
