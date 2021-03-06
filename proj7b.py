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
Builds a sentence with the given length, using the Bogensberger-Johnson
Technique.

Params: dictionary of cumulative frequencies, desired sentence length.
Returns: a sentence with the given length.
"""
def buildUnigramSentence(cumFrequencies, length):
    # converts cumFrequencies to a tuple of words and their cumulative
    # probability.
    cumFrequencies = sorted(cumFrequencies.items(), key=lambda x: x[1])
    for gram in cumFrequencies:
        if gram[0] == "<s>" or gram[0] == "</s>":
            cumFrequencies.remove(gram)
    sentence = ""
    for i in range(length):
        value = random.uniform(0.0,1)
        for word in cumFrequencies:
            if word[1] > value:
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

"""
Builds a sentence with the given length, using the Bogensberger-Johnson
Technique and Unigrams. Assumes that these are not unigrams.

Params: dictionary of cumulative frequencies, desired sentence length.
Returns: a sentence with the given length.
"""
def buildNgramSentence(cumFrequencies, length):

    # converts cumFrequencies to a tuple of words and their cumulative
    # probability.
    cumFrequencies = sorted(cumFrequencies.items(), key=lambda x: x[1])

    sentence = ""
    while True:
        startFound = False
        value = random.uniform(0.0,1)
        for word in cumFrequencies:
            if word[1] > value and word[0][:3] == "<s>":
                sentence += word[0][4].upper() + word[0][5:] + " "#word[0][:3] + word[0][4].upper() + word[0][5:] + " "
                startFound = True
                break
        if startFound:
            break

    for i in range(1,length-1):
        while True:
            startFound = True
            value = random.uniform(0.0,1)
            for word in cumFrequencies:
                if word[1] > value and "s>" not in word[0]:
                    sentence += word[0] + " "
                    startFound = False
                    break
            if not startFound:
                break

    while True:
        stopFound = False
        value = random.uniform(0.0,1)
        for word in cumFrequencies:
            if word[1] > value and word[0][-4:] == "</s>":
                #sentence += word[0][:-5] + "." + "</s>"
                sentence += word[0][:-5] + "."

                stopFound = True
                break
        if stopFound:
            break

    return sentence

if __name__ == "__main__":

    # UNPICKLE DICTIONARIES
    print "Retrieving data from pickled file."

    file = open("proj7b.pkl", "rb")
    unigramsCumFreq, bigramsCumFreq, trigramsCumFreq, quadgramsCumFreq = \
        pickle.load(file)
    file.close()

    numSentences = 5

    wholeUnigramSentence = ""
    wholeBigramSentence = ""
    wholeTrigramSentence = ""
    wholeQuadgramSentence = ""

    #PRINT SENTENCES
    print "\nUnigram sentences:"
    for i in range(numSentences):
        wholeUnigramSentence = buildUnigramSentence(unigramsCumFreq, 12) + " " + wholeUnigramSentence
    print wholeUnigramSentence

    print "\nBigram sentences:"
    for i in range(numSentences):
        wholeBigramSentence = buildNgramSentence(bigramsCumFreq, 6) + " " + wholeBigramSentence
    print wholeBigramSentence

    print "\nTrigram sentences:"
    for i in range(numSentences):
        wholeTrigramSentence = buildNgramSentence(trigramsCumFreq, 4) + " " + wholeTrigramSentence
    print wholeTrigramSentence

    print "\nQuadgram sentences:"
    for i in range(numSentences):
        wholeQuadgramSentence = buildNgramSentence(quadgramsCumFreq, 3) + " " + wholeQuadgramSentence
    print wholeQuadgramSentence
