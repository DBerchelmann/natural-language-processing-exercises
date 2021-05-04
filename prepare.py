import unicodedata
import re
import json
import bs4

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd



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


def tokenize():
    
    ''' This function utilizes tokenizer tool and returns a transformed string '''
    
    article = basic_clean(string)
    
    article = tokenizer.tokenize(article, return_str = True)
    
    return article


def stem():
    
    '''this function utilized the Porter Stemmer and returns a string '''
    
    article = tokenize()
    
    stems = [ps.stem(word) for word in article.split()]
    print(stems[:10])
    
    article_stemmed = ' '.join(stems)
    
    return article_stemmed



def lemmatize():
    
    ''' This function takes in tokenized content and the applicted lemmatization. It returns content that has been
    transformed by lemmatize '''
    
    article = tokenize()
    
    lemmas = [wnl.lemmatize(word) for word in article.split()]
    print(lemmas[:10])
    
    article_lemmatized = ' '.join(lemmas)
    
    return article_lemmatized



def remove_stopwords(extra_words=[], exclude_words=[]):
    
    ''' This function takes a lemmatized body of content and then applies stopwords to remove any unesscary word elements. 
    It returns an article without any stopwords. '''
    
    
    # brings in content that has been lemmatized
    article_lemmatized = lemmatize()
    
    # standard English language stopwords list from nltk
    stopword_list = stopwords.words('english')
    
    # add words to stopword list
    
    stopword_list = stopword_list + exclude_words
    
    # remove stopwords from stopword list
    
    # stopword_list = stopword_list - extra_words
    
 
    # Split words in lemmatized article.
    words = article_lemmatized.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings; assign to a variable to keep changes.
    article_without_stopwords = ' '.join(filtered_words)
    
    
    return article_without_stopwords