"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 4: This project accepts a name as input and gives the encoded form as
output.
Due: 28 September 2018
Usage: python proj4.py # should be Python 2.7
"""

import re

def soundex(name):
    expression = replaceWithNumbers(name)
    print expression
    expression = removeDuplicateNumbers(expression)
    print expression
    expression = makeFormLetterDigitx3(expression)
    return expression

"""
Cited source: https://stackoverflow.com/questions/4574509/remove-duplicate-chars-using-regex
"""
def removeDuplicateNumbers(name):
    expression = re.sub(r'([a-z])\1+', r'\1', name)
    return expression

def makeFormLetterDigitx3(expression):
    if len(expression) < 4:
        while len(expression) < 4:
            expression += '0'
    elif len(expression) > 4:
        expression = expression[:4]
    return expression

def replaceWithNumbers(name):
    expression = name[1:]
    expression = re.sub(r'([a,e,h,i,o,u,w,y])', r'', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([b,f,p,v])', r'1', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([c,g,j,k,q,s,x,z])', r'2', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([d,t])', r'3', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([l])', r'4', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([m,n])', r'5', expression, flags=re.IGNORECASE)
    print expression
    expression = re.sub(r'([r])', r'6', expression, flags=re.IGNORECASE)
    print expression
    expression = name[0] + expression
    return expression

if __name__ == '__main__':
    name = raw_input("Please enter a name: ").replace(' ', '')
    expression = soundex(name)
    print expression
