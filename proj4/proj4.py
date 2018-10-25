"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 4: This project accepts a name as input and gives the encoded form as
output.
Due: 28 September 2018
Usage: python proj4.py <name>
should be Python 2.7
"""

import re
import sys

'''
call helper functions to walk through
the soundex algorithm.
'''
def soundex(name):
    expression = replaceWithNumbers(name)
    expression = removeDuplicateNumbers(expression)
    expression = makeFormLetterDigitx3(expression)
    return expression

"""
Removes duplicate numbers from format
ex: in Jurafsky, J6122 becomes J612

Cited source: https://stackoverflow.com/questions/4574509/remove-duplicate-chars-using-regex
"""
def removeDuplicateNumbers(expression):
    # detects occurences of:
	# 11, 22, 33, 44, 55, 66, 77 at the end of a string
    expression = re.sub(r'([1]{2})', r"1", expression)
    expression = re.sub(r'([2]{2})', r"2", expression)
    expression = re.sub(r'([3]{2})', r"3", expression)
    expression = re.sub(r'([4]{2})', r"4", expression)
    expression = re.sub(r'([5]{2})', r"5", expression)
    expression = re.sub(r'([6]{2})', r"6", expression)
    return expression

'''
Removes any more than three numbers from format
ex: A1234 becomes A123
'''
def makeFormLetterDigitx3(expression):
    if len(expression) < 4:
        while len(expression) < 4:
            expression += '0'
    elif len(expression) > 4:
        expression = expression[:4]
    return expression

'''
Removes specified letters
Replaces letters with specified digits
(noted in internal comments)
'''
def replaceWithNumbers(name):

    # to keep the first letter of the word
    # by starting 'expression' after first letter
    # of input string
    expression = name[1:]

    # to remove a, e, h, i, o, u, w, y
    expression = re.sub(r'([a,e,h,i,o,u,w,y])', r'', expression, flags=re.IGNORECASE)

    # to replace b, f, p, v with 1
    expression = re.sub(r'([b,f,p,v])', r'1', expression, flags=re.IGNORECASE)

    # to replace c, g, j, k, q, s, x, z with 2
    expression = re.sub(r'([c,g,j,k,q,s,x,z])', r'2', expression, flags=re.IGNORECASE)

    # to replace d, t with 3
    expression = re.sub(r'([d,t])', r'3', expression, flags=re.IGNORECASE)

    # to replace l with 4
    expression = re.sub(r'([l])', r'4', expression, flags=re.IGNORECASE)

    # to replace m, n with 5
    expression = re.sub(r'([m,n])', r'5', expression, flags=re.IGNORECASE)

    # to replace r with 6
    expression = re.sub(r'([r])', r'6', expression, flags=re.IGNORECASE)

    # to reattach first letter of
    # input string to 'expression'
    expression = name[0] + expression
    print "Replaced with numbers:", expression
    return expression

if __name__ == '__main__':

    # first arg is input string
    name = sys.argv[1]

    # start soundex algorithm on input string
    expression = soundex(name)

    # return name and expression mapping
    print name + " -> " + expression
