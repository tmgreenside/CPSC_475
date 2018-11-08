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
Technique and Unigrams.

Params: dictionary of cumulative frequencies, desired sentence length.
Returns: a sentence with the given length.
"""
def buildNgramSentence(cumFrequencies, length, includeMarkers=False):
    # converts cumFrequencies to a tuple of words and their cumulative
    # probability.
    cumFrequencies = sorted(cumFrequencies.items(), key=lambda x: x[1])
    sentence = ""
    if includeMarkers:
        sentence += "<s>"
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
    if includeMarkers:
        sentence += "</s>"
    return sentence


if __name__ == "__main__":

    # UNPICKLE DICTIONARIES
    print "Retrieving data from pickled file."

    file = open("proj7b.pkl", "rb")
    unigramsCumFreq, bigramsCumFreq, trigramsCumFreq, quadgramsCumFreq = \
        pickle.load(file)
    file.close()

    numSentences = 5

    markers = raw_input("Would you like to include start and end markers? (Y/N)\n")
    if "y" in markers.lower():
        includeMarkers = True
    else:
        includeMarkers = False

    #PRINT SENTENCES
    print ""
    print "Unigram sentences:"
    for i in range(numSentences):
        unigramSentence = buildNgramSentence(unigramsCumFreq, 12)
        print(unigramSentence)
    print ""
    print "Bigram sentences:"
    for i in range(numSentences):
        bigramSentence = buildNgramSentence(bigramsCumFreq, 6, includeMarkers)
        print(bigramSentence)
    print ""
    print "Trigram sentences:"
    for i in range(numSentences):
        trigramSentence = buildNgramSentence(trigramsCumFreq, 4, includeMarkers)
        print(trigramSentence)
    print ""
    print "Quadgram sentences:"
    for i in range(numSentences):
        quadgramSentence = buildNgramSentence(quadgramsCumFreq, 3, includeMarkers)
        print(quadgramSentence)
