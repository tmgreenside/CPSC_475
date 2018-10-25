"""
Team Member #1: Trevor Greenside
Team Member #2: Carol Joplin
Zagmail address for team member 1: tgreenside@zagmail.gonzaga.edu
Zagmail address for team member 2: cjoplin@zagmail.gonzaga.edu
Project 2: This project reads a text document supplied by the user
and displays the number of instances of the substring.
Due: 7 September 2018

To run: run with Python in the terminal (command: python proj2.py)
"""

import os

# This function continually takes input from the user until the user provides
# a valid filename present in the directory
def getFileName():
    while True:
        filename = raw_input("Please enter a file name(do not use parentheses): ")
        if ".txt" not in filename:
            print("Please enter a file name for a .txt file.")
        elif not os.path.isfile(filename):
            print("File not found.")
        else:
            return filename

# This function opens and returns a file
def openFile(filename):
    return open(filename, "r")

# This function saves each line in the file as a string in a list.
# Returns: list of strings.
def readFileToList(file):
    lines = []
    while True:
        line = file.readline().replace('\n', ' ')
        if not line:
            break
        lines.append(line)
    return lines

# This function takes as input the list of file lines, and the substring
# provided by the user and returns the number of instances present in the
# file.
def countSubstringOccurrences(substring, stringList):
    counter = 0
    for string in stringList:
        for i in range(len(string) - len(substring)):
            if string[i] == substring[0]:
                if searchSub(string, i, substring):
                    counter += 1
    return counter

# This function returns true if a substring is present starting at the
# given index of a string, false otherwise.
def searchSub(string, stringIndex, substring):
    subIndex = 0
    while subIndex < len(substring):
        if string[stringIndex] == substring[subIndex]:
            subIndex += 1
            stringIndex += 1
        else:
            return False
    return True

if __name__ == '__main__':
    filename = getFileName()
    file = openFile(filename)
    stringList = readFileToList(file)
    substring = raw_input("Please enter a substring: ")
    print(countSubstringOccurrences(substring, stringList))
    file.close()
