"""
Team Member #1: Trevor Greenside
Team Member #2: None
Zagmail address for Team Member #1: tgreenside@zagmail.gonzaga.edu
Project 6: This project focuses on unigrams and uses statistics via
the Bogensberger-Johnson Cumulative Probability Technique to construct
sentences.
Due: 24 October 2018
Usage: python proj6.py
"""

import nltk
import random
from nltk.corpus import brown

"""
Retrieves, tokenizes, and returns the Brown Editorial corpus.

Params: none.
Returns: tokenized Brown Editorial corpus.
"""
def tokenizedBrown():
    tmp = brown.sents(categories='editorial')
    new = [[item.encode('ascii') for item in lst] for lst in tmp]
    # remove periods and make all characters lowercase
    for sentence in new:
        for word in sentence:
            if word == '.':
                sentence.remove(word)
    return [[word.lower() for word in sentence] for sentence in new]

"""
Takes a tokenized corpus and returns a dictionary containing the number
of occurrences for each word.

Params: tokenized corpus.
Returns: dictionary with word counts.
"""
def getWordCounts(tokenizedCorpus):
    wordCounts = {}
    for sentence in tokenizedCorpus:
        for word in sentence:
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
    return wordCounts

"""
Gets the total word count of a corpus, including repeats.

Params: none.
Returns: word count.
"""
def getTotalWordCount(tokenizedCorpus):
    return sum([len(sentence) for sentence in tokenizedCorpus])

"""
Takes a dictionary containing word counts and a corpus' total word count
as input, and returns a dictionary containing the percentage of words in
the corpus that are a particular word.

Params: dictionary of counted word occurences, corpus total word count.
Returns: dictionary of relative frequencies.
"""
def getRelFrequencies(wordCounts, totalWordCount):
    relFrequencies = {}
    for word in wordCounts:
        relFrequencies[word] = float(wordCounts[word]) / float(totalWordCount)
    return relFrequencies

"""
Takes a dictionary of relative frequencies and calculates a cumulative
frequency dictionary.

Params: dictionary of relative frequencies.
Returns: dictionary of cumulative frequencies.
"""
def getCumFrequencies(relFrequencies):
    cumFrequencies = {}
    previous = 0.0
    for word in relFrequencies:
        cumFrequencies[word] = previous + float(relFrequencies[word])
        previous = previous + float(relFrequencies[word])
    return cumFrequencies

"""
Builds a sentence with the given length, using the Bogensberger-Johnson
Technique.

Params: dictionary of cumulative frequencies, desired sentence length.
Returns: a sentence with the given length.
"""
def buildSentence(cumFrequencies, length):
    sentence = ""
    for i in range(length):
        value = random.uniform(0.0,1)
        print "Value:", value
        for word in cumFrequencies:
            if cumFrequencies[word] > value:
                if i == 0:
                    firstWord = ""
                    firstWord += word[0].upper()
                    firstWord += word[1:]
                    sentence += firstWord
                else:
                    sentence += " " + word
                break
    sentence += "."
    return sentence

if __name__ == "__main__":
    print "Starting."
    tokenized = tokenizedBrown()
    totalWordCount = getTotalWordCount(tokenized)
    wordCounts = getWordCounts(tokenized)
    relFrequencies = getRelFrequencies(wordCounts, totalWordCount)
    cumFrequencies = getCumFrequencies(relFrequencies)

    for i in range(5):
        print(buildSentence(cumFrequencies, 10))
