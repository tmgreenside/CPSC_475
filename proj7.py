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
    file = open(fileName)
    text = getFileContents(file)
    file.close()
    new = []
    for line in text:
        if line.lstrip() != "":
            for char in ['.','!','?',',','"','`','/','[',']',
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
Create monograms from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateMonograms(tokenizedCorpus):
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
            if (tokens[i][j], tokens[i][j+1]) not in bigrams:
                bigrams[(tokens[i][j], tokens[i][j+1])] = 1
            else:
                bigrams[(tokens[i][j], tokens[i][j+1])] += 1

    return bigrams

"""
Create trigrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateTrigrams(tokens):
    trigrams = {}

    for i in range (len(tokens)):
        for j in range(len(tokens[i]) - 2):
            if (tokens[i][j], tokens[i][j+1], tokens[i][j+2]) not in bigrams:
                bigrams[(tokens[i][j], tokens[i][j+1], tokens[i][j+2])] = 1
            else:
                bigrams[(tokens[i][j], tokens[i][j+1], tokens[i][j+2])] += 1

    return trigrams

"""
Create trigrams from the tokenized list. Create a data structure that holds
the grams and their occurence counts.
"""
def generateQuadgrams(tokens):
    quadgrams = {}

    for i in range (len(tokens)):
        for j in range(len(tokens[i]) - 3):
            if (tokens[i][j], tokens[i][j+1], tokens[i][j+2], tokens[i][j+3]) not in bigrams:
                bigrams[(tokens[i][j], tokens[i][j+1], tokens[i][j+2], tokens[i][j+3])] = 1
            else:
                bigrams[(tokens[i][j], tokens[i][j+1], tokens[i][j+2], tokens[i][j+3])] += 1

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
FILLTYPES

fill the types list with unique tokens.
loop through tokens to find unique occurences of each word
"""
def fillTypes(types, tokens):
    for word in tokens:
        if word not in types:
            types.append(word)

    totalTypes = len(types)

    return types, totalTypes

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

# """
# CALCULATE PROBABILITIES
# calculate probability and cumulativeProbability
# """
# def calculateProbabilities(tokens, types, totalTokens, totalTypes, prob, probPrev, cumulativeProb, cumulativeProbPrev, word, dictionary):
#
#     #typeCount: used for calculating probability
#
#     for type in types:
#         word = type
#         typeCount = 0.0
#         prob = 0.0
#         for token in tokens:
#             if token == type:
#                 typeCount += 1.0
#
#         # Probability = number of appearances / number of tokens
#         prob = typeCount / totalTokens
#         probPrev = prob
#
#         # Cumulative Probability = (cumulativeProbability + prob) of i-1
#         cumulativeProb = probPrev + cumulativeProbPrev
#         cumulativeProbPrev = cumulativeProb
#
#     dictionary.update({word : (prob, cumulativeProb)})
#
#     return dictionary



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

"""
Builds a sentence with the given length, using the Bogensberger-Johnson
Technique and Monograms.

Params: dictionary of cumulative frequencies, desired sentence length.
Returns: a sentence with the given length.
"""
def buildMonogramSentence(cumFrequencies, length):
    # converts cumFrequencies to a tuple of words and their cumulative
    # probability.
    cumFrequencies = sorted(cumFrequencies.items(), key=lambda x: x[1])
    sentence = ""
    for i in range(length):
        value = random.uniform(0.0,1)
        for word in cumFrequencies:
            if word[1] > value and word[0] != "<s>" and word[0] != "</s>":
                if i == 0:
                    firstWord = ""
                    firstWord += word[0][0].upper()
                    firstWord += word[0][1:]
                    sentence += firstWord
                else:
                    sentence += " " + word[0]
                break
    sentence += "."
    return sentence

def buildNgramSentence(cumFrequencies, length):
    sentence = ""

    return sentence

if __name__ == "__main__":
    tokens = tokenizeShakespeare("100-0.txt")
    monograms = generateMonograms(tokens)
    monogramsRelFreq = getRelFrequencies(monograms, getNgramCount(monograms))
    monogramsCumFreq = getCumFrequencies(monogramsRelFreq)
    print "Monograms generated."
    bigrams = generateBigrams(tokens)
    print "Bigrams generated."
    trigrams = generateTrigrams(tokens)
    print "Trigrams generated."
    quadgrams = generateQuadgrams(tokens)
    print "Quadgrams generated."
    print ""
    print "Monogram sentences:"
    for i in range(5):
       print(buildMonogramSentence(monogramsCumFreq, 10))
