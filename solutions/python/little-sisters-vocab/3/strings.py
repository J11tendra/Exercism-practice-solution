"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return 'un'+word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    emp = vocab_words[0]
    separator = ' :: '
    for word in vocab_words[1:]:
        emp += ',' + vocab_words[0] + word

    return separator.join(emp.split(','))
    


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    # slice the string without the 'ness' suffix
    # if in the sliced string if the last element is vowel change it to y.
    # else do nothing

    root_word = word[:-4]
    # vowels = ['a', 'e', 'i', 'o', 'u']
    # for vowel in vowels:
    if 'i' == root_word[-1]:
        return root_word[:-1] + 'y'

    return root_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    # first split the string with space
    # access the given indexed word
    # add a suffix to the word and return

    suffix = 'en'
    target_word = sentence[:-1].split(" ")
    target_word = target_word[index]+suffix
    return target_word
