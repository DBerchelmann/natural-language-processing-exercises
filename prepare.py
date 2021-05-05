import unicodedata
import re
import json
import bs4

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd




~~~~~~~~~~~~~~~~~Prepare_for_NLP~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def basic_clean(string):
    
    features="lxml"
        
    original = string
    article = original.lower()
    
    # Remove inconsistencies in unicode character encoding.
    # encode the strings into ASCII bytestrings (ignore non-ASCII characters)
    # decode the bytestring into (Unicode) string

    article = unicodedata.normalize('NFKD', article)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    article = re.sub(r"[^a-z0-9'\s]", '', article)
    #article = article.replace('\n', ' ')
    
    
    return article


def tokenize(string):
    
    ''' This function utilizes tokenizer tool and returns a transformed string '''
    
    article = basic_clean(string)
    
    article = tokenizer.tokenize(article, return_str = True)
    
    return article


def stem(string):
    
    '''this function utilized the Porter Stemmer and returns a string '''
    
    article = tokenize()
    
    stems = [ps.stem(word) for word in article.split()]
    print(stems[:10])
    
    article_stemmed = ' '.join(stems)
    
    return article_stemmed



def lemmatize(string):
    
    ''' This function takes in tokenized content and the applicted lemmatization. It returns content that has been
    transformed by lemmatize '''
    
    article = tokenize()
    
    lemmas = [wnl.lemmatize(word) for word in article.split()]
    print(lemmas[:10])
    
    article_lemmatized = ' '.join(lemmas)
    
    return article_lemmatized



def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords