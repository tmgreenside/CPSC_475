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

def buildNgramSentence(cumFrequencies, length):

    # converts cumFrequencies to a tuple of words and their cumulative
    # probability.
    cumFrequencies = sorted(cumFrequencies.items(), key=lambda x: x[1])
    
    sentence = ""
    for i in range(length):
        # random value
        value = random.uniform(0.0,1)
        for word in cumFrequencies:
            if word[1] > value:
                while word[0][:3] == "<s>":
                    if i == 0:
                        firstWord = ""
                        firstWord += word[0][3].upper()
                        firstWord += word[0][4:]
                        sentence += firstWord
                    else:
                        sentence += " " + word[0]
                    break
    sentence += "."
    return sentence


if __name__ == "__main__":

    # UNPICKLE DICTIONARIES
    print "Retrieving data from pickled file."

    file = open("proj7b.pkl", "rb")
    unigramsCumFreq, bigramsCumFreq, trigramsCumFreq, quadgramsCumFreq = \
        pickle.load(file)
    file.close()

    numSentences = 5

    #wholeUnigramSentence = ""
    #wholeBigramSentence = ""
    #wholeTrigramSentence = ""
    wholeQuadgramSentence = ""
    
    #PRINT SENTENCES
    """print ""
    print "Unigram sentences:"
    for i in range(numSentences):
        unigramSentence = buildNgramSentence(unigramsCumFreq, 12)
        wholeUnigramSentence = wholeUnigramSentence + " " + unigramSentence
    print(wholeUnigramSentence)
    print ""
    print "Bigram sentences:"
    for i in range(numSentences):
        bigramSentence = buildNgramSentence(bigramsCumFreq, 6)
        wholeBigramSentence = wholeBigramSentence + " " + bigramSentence
    print(wholeBigramSentence)
    print ""
    print "Trigram sentences:"
    for i in range(numSentences):
        trigramSentence = buildNgramSentence(trigramsCumFreq, 4)
        wholeTrigramSentence = wholeTrigramSentence + " " + trigramSentence
    print(wholeTrigramSentence)
    print "" """
    print "Quadgram sentences:"
    for i in range(numSentences):
        quadgramSentence = buildNgramSentence(quadgramsCumFreq, 3)
        wholeQuadgramSentence = wholeQuadgramSentence + " " + quadgramSentence
    print(wholeQuadgramSentence)
