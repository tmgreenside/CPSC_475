"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 2: This project
Due: … (enter official due date as found on the class schedule)
"""

import nltk, re, pickle
from nltk.corpus import inaugural

def getAddressesAsWords():
    addresses = []
    for address in inaugural.fileids():
        file = inaugural.raw(address) # gives full address as a long string
        print(file)
        file = tokenize(file)
        addresses.append(file.split())
    return addresses

# taken from De Palma ex11.py
def tokenize(line):
    string = re.sub('\n',' ', line)
     #create a list containing all lower case characters
    good_chars = [chr(value) for value in range(ord('a'),ord('z') + 1,1)]
    good_chars.append(' ')
    string = string.lower()
    new_str = ''
    for ch in string:
        if ch in good_chars:
            new_str = new_str + ch
    return new_str

def pickleInauguralLists(list, filename):
    file = open(filename, "wb")
    pickle.dump(list, file)
    file.close()

if __name__ == '__main__':
    lists = getAddressesAsWords()
    pickleInauguralLists(lists, "proj3.pkl")
