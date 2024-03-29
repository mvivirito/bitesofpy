"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
from string import punctuation as punc

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def clean_string(wordinput):
    table = str.maketrans({key: None for key in punc})
    word = (wordinput.translate(table))
    word = word.lower()
    word = word.replace(' ', '')
    word = word.replace('’', '')
    return(word)

def reverse_string(wordinput):
    characters = []
    for x in wordinput:
        characters.insert(0, x)
        word = ""
        for x in characters:
            word += x

    return(word)

def is_palindrome(wordin):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    cleanword = clean_string(wordin)
    if cleanword == reverse_string(cleanword):
        return(cleanword)

def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    if words == None:
        words = load_dictionary()

    longest = ""
    length = 0

    for word in words:
        if (is_palindrome(word) != None) and (len(word) > length):
            longest = word
            length = len(word)

    return(longest)


