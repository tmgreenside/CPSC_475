"""
Team Member #1: Trevor Greenside
Team Member #2: None
Zagmail address for Team Member #1: tgreenside@zagmail.gonzaga.edu
Project 6: This project uses statistics, unigrams, bigrams, trigrams, and
quadgrams via the Bogensberger-Johnson Cumulative Probability Technique to
construct sentences.
Due: 24 October 2018
Usage: python proj6.py
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

if __name__ == "__main__":
    tokens = tokenizeShakespeare("100-0.txt")
