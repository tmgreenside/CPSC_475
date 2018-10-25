"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 2: This project
Due: … (enter official due date as found on the class schedule)
"""

import nltk, re, pickle
import matplotlib.pyplot as plt
from nltk.corpus import inaugural

def getWord():
    word = ""
    while len(word) == 0:
        word = input("Please enter a word: ").replace(" ", "")
    return word

def buildFreqTable(word, lists):
    freq = []
    years = []
    for filename in inaugural.fileids():
        years.append(int(filename[0:4]))
    assert(len(lists) == len(years))
    for i in range(len(years)):
        counter = 0
        for listWord in lists[i]:
            if listWord == word:
                counter += 1
        freq.append(counter)
    return (freq, years)

def buildPlot(word, lists):
    freq, years = buildFreqTable(word, lists)
    plt.plot(years, freq)
    plt.xlabel("Inauguration Year")
    plt.ylabel("Num. Occurences")
    plt.show() # Yes, this looks sideways, but it's what his instructions said

if __name__ == '__main__':
    addresssIn = open("proj3.pkl","rb")
    addresses = pickle.load(addresssIn)
    addresssIn.close()

    word = getWord()

    buildPlot(word, addresses)

    print(word, "is a thing")
