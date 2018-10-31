"""
Team Member #1: Trevor Greenside
Team Member #2: Carol Joplin
Zagmail address for Team Member #1: tgreenside@zagmail.gonzaga.edu
Project 6: This project uses statistics, unigrams, bigrams, trigrams, and
quadgrams via the Bogensberger-Johnson Cumulative Probability Technique to
construct sentences.
Due: 24 October 2018
Usage: python proj6.py
"""
import random

"""
GET FILE CONTENTS

gets file contents and reads into a list called 'lines'
"""
def getFileContents(file):
    lines = []
    while True:
        line = file.readline()
        if line:
            lines.append(line)
        else:
            break
    return lines

"""
TOKENIZE SHAKESPEARE

strip various punctuation
all words to lowercase
append <s> to start
append </s> to end
"""
def tokenizeShakespeare(fileName):
    file = open(fileName)
    text = getFileContents(file)
    file.close()
    new = []
    for line in text:
        if line.lstrip() != "":
            for char in ['.','!','?',',','"','`','/',
            '\\','-','_',':',';','``','(',')','--','\'\'']:
                if char in line:
                    line = line.replace(char, "")
            line = line.lower().split()
            newline = ["<s>"]
            for word in line:
                newline.append(word)
            newline.append("</s>")
            new.append(newline)
    return new

"""
TODO: 4. Generate Grams

Create unigrams, bigrams, trigrams, and quadgrams from the tokenized list.
Compute their probabilities and cumulative probabilities
Create a data structure that holds the grams and their cumulative probabilities
"""
def generateGrams(tokens):
    # setup variables
    # tokens list created in main

    # unique words, bigrams, trigrams, quadgrams
    types = []

    # CREATE UNIGRAMS
    unigrams = {}

    # totalTokens: amount of tokens in the tokens list
    totalTokens = len(tokens)

    # fill types list and find totalTypes: amount of types in the types list
    types, totalTypes = fillTypes(types, tokens)

    # Calculate the probabilties
    calculateProbabilities(tokens, types, totalTokens, totalTypes, prob, probPrev, cumulativeProb, cumulativeProbPrev, word, unigrams)

    # CREATE BIGRAMS
    # create 2-tuples as key for bigrams dictionary
    bigrams = {}

    # create 2-tuples?
    for i in :
        for i in range(2):
            t1 = (


    # CREATE TRIGRAMS
    # create 3-tuples as key for trigrams dictionary
    trigrams = {}

    # CREATE QUADGRAMS
    # create 4-tuples as key for quadgrams dictionary
    quadgrams = {}

"""
    FILLTYPES

    fill the types list with unique tokens
    loop through tokens to find unique occurences of each word
"""
def fillTypes(types, tokens):
    for word in tokens:
        if word not in types:
            types.append(word)

totalTypes = len(types)

return types, totalTypes

"""
CALCULATE BIGRAMS
"""
def calculateBigrams(tokens, bigrams):

    return bigrams

"""
CALCULATE TRIGRAMS
"""
def calculateTrigrams(tokens, trigrams):

    return trigrams

"""
CALCULATE QUADGRAMS
"""
def calculateQuadgrams(tokens, quadgrams):

    return quadgrams

"""
CALCULATE PROBABILITIES
calculate probability and cumulativeProbability
"""
def calculateProbabilities(tokens, types, totalTokens, totalTypes, prob, probPrev, cumulativeProb, cumulativeProbPrev, word, dictionary):

    #typeCount: used for calculating probability

    for type in types:
        word = type
        typeCount = 0.0
        prob = 0.0
        for token in tokens:
            if token == type:
                typeCount +=1.0

        # Probability = number of appearances / number of tokens
        prob = typeCount / totalTokens
        probPrev = prob

        # Cumulative Probability = (cumulativeProbability + prob) of i-1
        cumulativeProb = probPrev + cumulativeProbPrev
        cumulativeProbPrev = cumulativeProb

    dictionary.update({word : (prob, cumulativeProb)})

    return dictionary



"""
    TODO: 5. Generate Grams Sequences

    For each gram type, generate random sentences using the Bogensberg-Johnson technique. The
    first word in each sentence is capitalized.  The sentence ends with a period.  All sentences appear on a single line.

    Sentence Length:
        unigrams: 12 words
        bigrams: 6 bigrams
        trigrams: 4 trigrams
        quadgrams: 3 quagrams
"""

if __name__ == "__main__":
    tokens = tokenizeShakespeare("100-0.txt")
