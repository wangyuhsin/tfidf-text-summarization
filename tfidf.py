import sys

import nltk
from nltk.stem.porter import *
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import xml.etree.cElementTree as ET
from collections import Counter
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import zipfile
import os


def gettext(xmltext) -> str:
    """
    Parse xmltext and return the text from <title> and <text> tags
    """
    xmltext = xmltext.encode(
        "ascii", "ignore")  # ensure there are no weird char
    root = ET.fromstring(xmltext)
    title = root[0].text
    text = ""
    for element in root.iterfind(".//text/*"):
        text += element.text + " "
    return title + " " + text[:-1]


def tokenize(text) -> list:
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3, strip digits.
    """
    text = text.lower()
    text = re.sub("[" + string.punctuation + "0-9\\r\\t\\n]", " ", text)
    tokens = nltk.word_tokenize(text)
    tokens = [w for w in tokens if len(w) > 2]  # ignore a, an, to, at, be, ...
    tokens = [w for w in tokens if w not in ENGLISH_STOP_WORDS]
    return tokens


def stemwords(words) -> list:
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """
    stemmer = PorterStemmer()
    stem = [stemmer.stem(w) for w in words]
    return stem


def tokenizer(text) -> list:
    return stemwords(tokenize(text))


def compute_tfidf(corpus: dict) -> TfidfVectorizer:
    """
    Create and return a TfidfVectorizer object after training it on
    the list of articles pulled from the corpus dictionary. Meaning,
    call fit() on the list of document strings, which figures out
    all the inverse document frequencies (IDF) for use later by
    the transform() function. The corpus argument is a dictionary
    mapping file name to xml text.
    """
    tfidf = TfidfVectorizer(
        input="content",
        analyzer="word",
        preprocessor=gettext,
        tokenizer=tokenizer,
        stop_words="english",  # even more stop words
        decode_error="ignore",
    )
    tfidf = TfidfVectorizer(
        input="content",
        analyzer="word",
        preprocessor=gettext,
        tokenizer=tokenizer,
        stop_words="english",
        decode_error="ignore",
    )
    texts = []
    for key in corpus.keys():
        texts.append(corpus[key])
    tfidf.fit(texts)
    return tfidf


def summarize(tfidf: TfidfVectorizer, text: str, n: int):
    """
    Given a trained TfidfVectorizer object and some XML text, return
    up to n (word,score) pairs in a list. Discard any terms with
    scores < 0.09. Sort the (word,score) pairs by TFIDF score in reverse order.
    """
    return_lst = []
    tfidf_matrix = tfidf.transform([text])
    word_indexes = tfidf_matrix.nonzero()[1]
    for index in word_indexes:
        if float(tfidf_matrix.T.todense()[index]) >= 0.09:
            return_lst.append(
                (
                    tfidf.get_feature_names_out()[index],
                    float(tfidf_matrix.T.todense()[index]),
                )
            )
    return_lst = sorted(return_lst, key=lambda x: x[1], reverse=True)[:n]
    return return_lst


def load_corpus(zipfilename: str) -> dict:
    """
    Given a zip file containing root directory reuters-vol1-disk1-subset
    and a bunch of *.xml files, read them from the zip file into
    a dictionary of (filename,xmltext) associations. Use namelist() from
    ZipFile object to get list of xml files in that zip file.
    Convert filename reuters-vol1-disk1-subset/foo.xml to foo.xml
    as the keys in the dictionary. The values in the dictionary are the
    raw XML text from the various files.
    """
    return_dict = {}
    with zipfile.ZipFile(zipfilename, mode="r") as archive:
        for filename in archive.namelist():
            if filename.endswith(".xml"):
                text = ""
                with open(filename, "r") as f:
                    for line in f:
                        text += str(line)
                return_dict[filename.split("/")[1]] = text
    return return_dict
