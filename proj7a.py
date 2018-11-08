"""
Team Member #1: Trevor Greenside
Team Member #2: Carol Joplin
Zagmail address for Team Member #1: tgreenside@zagmail.gonzaga.edu
Project 7: This project uses statistics, unigrams, bigrams, trigrams, and
quadgrams via the Bogensberger-Johnson Cumulative Probability Technique to
construct sentences.
Due: 9 November 2018
Usage: python proj7.py
"""
import random, copy, pickle

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
Gets the total word count of a corpus, including repeats.

Params: none.
Returns: word count.
"""
def getTotalWordCount(tokenizedCorpus):
    return sum([len(sentence) for sentence in tokenizedCorpus])

"""
TOKENIZE SHAKESPEARE

strip various punctuation
all words to lowercase
append <s> to start
append </s> to end
"""
def tokenizeShakespeare(fileName):
    file = open(fileName,"r")
    text = getFileContents(file)
    file.close()
    new = []
    for line in text:
        if line.lstrip() != "":
            for char in ['.','!','?',',','"','`','/','[',']',
                        '\\','-','_',':',';','``','(',')','--',
                         '\'\'', '', '\n']:
                if char in line:
                    line = line.replace(char, "")
            line = line.lower().split()
            newline = ["<s>"]
            newline = []
            for word in line:
                newline.append(word)
            newline.append("</s>")
            new.append(newline)
    return new

"""
Create unigrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateUnigrams(tokenizedCorpus):
    wordCounts = {}
    for sentence in tokenizedCorpus:
        for word in sentence:
            if word in wordCounts:
                wordCounts[word] += 1
            else:
                wordCounts[word] = 1
    return wordCounts

"""
Create bigrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateBigrams(tokens):
    bigrams = {}

    for i in range (len(tokens)):
        for j in range(len(tokens[i]) - 1):
            bi = tokens[i][j] + ' ' + tokens[i][j+1]
            if bi not in bigrams:
                bigrams[bi] = 1
            else:
                bigrams[bi] += 1

    return bigrams

"""
Create trigrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateTrigrams(tokens):
    trigrams = {}

    for i in range (len(tokens)):
        for j in range(len(tokens[i]) - 2):
            tri = tokens[i][j] + ' ' + tokens[i][j+1] + ' ' + tokens[i][j+2]
            if tri not in trigrams:
                trigrams[tri] = 1
            else:
                trigrams[tri] += 1

    return trigrams

"""
Create quadgrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateQuadgrams(tokens):
    quadgrams = {}

    for i in range (len(tokens)):
        for j in range(len(tokens[i]) - 3):
            quad = tokens[i][j] + ' ' + tokens[i][j+1] + ' ' + tokens[i][j+2] + ' ' + tokens[i][j+3]
            if quad not in quadgrams:
                quadgrams[quad] = 1
            else:
                quadgrams[quad] += 1

    return quadgrams

"""
Takes a dictionary of ngrams and their occurences and returns the total number
of ngram occurences in the dictionary.
"""
def getNgramCount(ngramsSet):
    count = 0
    for ngram in ngramsSet:
        count += ngramsSet[ngram]
    return count

"""
Takes a dictionary of ngrams and their occurence count and returns a dictionary
with the frequency of their occurence relative to the other ngrams.
"""
def getRelFrequencies(ngramCounts, totalNgramCount):
    relFrequencies = {}
    for ngram in ngramCounts:
        relFrequencies[ngram] = float(ngramCounts[ngram]) / float(totalNgramCount)
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
    for ngram in relFrequencies:
        cumFrequencies[ngram] = previous + float(relFrequencies[ngram])
        previous = previous + float(relFrequencies[ngram])
    return cumFrequencies


if __name__ == "__main__":

    # CREATE TOKENS
    tokens = tokenizeShakespeare("shakespeare.txt")

    # UNIGRAMS
    unigrams = generateUnigrams(tokens)
    unigramsRelFreq = getRelFrequencies(unigrams, getNgramCount(unigrams))
    unigramsCumFreq = getCumFrequencies(unigramsRelFreq)
    print "Unigrams generated."

    # BIGRAMS
    bigrams = generateBigrams(tokens)
    bigramsRelFreq = getRelFrequencies(bigrams, getNgramCount(bigrams))
    bigramsCumFreq = getCumFrequencies(bigramsRelFreq)
    print "Bigrams generated."

    #TRIGRAMS
    trigrams = generateTrigrams(tokens)
    trigramsRelFreq = getRelFrequencies(trigrams, getNgramCount(trigrams))
    trigramsCumFreq = getCumFrequencies(trigramsRelFreq)
    print "Trigrams generated."

    #QUADGRAMS
    quadgrams = generateQuadgrams(tokens)
    quadgramsRelFreq = getRelFrequencies(quadgrams, getNgramCount(quadgrams))
    quadgramsCumFreq = getCumFrequencies(quadgramsRelFreq)
    print "Quadgrams generated."

    # cumFrequencies = copy(unigramsCumFreq)
    # cumFrequencies.update(bigramsCumFreq)
    # cumFrequencies.update(trigramsCumFreq)
    # cumFrequencies.update(quadgramsCumFreq)

    cumFrequencies = (unigramsCumFreq, bigramsCumFreq, trigramsCumFreq,
                        quadgramsCumFreq)

    print "Dictionaries merged into one datastructure."
    print "Finishing."

    file = open("proj7b.pkl", "wb")
    pickle.dump(cumFrequencies, file)
    file.close()

    print "Done."
