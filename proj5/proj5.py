"""
Team Member #1: Carol Joplin
Team Member #2: Trevor Greenside
Zagmail address for team member 1: cjoplin@zagmail.gonzaga.edu
Project 5: This project accepts two words as command line input and displays
the minimum edit distance and the alignment from the minimum edit distance
computation.
Due: 5 October 2018
Usage: python proj5.py <source> <target>
# should be Python 2.7
"""

import re
import sys

INS_COST = 1
DEL_COST = 1

def sub_cost(sourceChar, targetChar):
    if sourceChar == targetChar:
        return 0
    return 2

# TO DO
def minEditDistance(source, target):
    n = len(target)
    m = len(source)
    distance = []
    distance.append([0])
    for i in range(1,n+1):
        distance.append([distance[i - 1][0] + INS_COST])
    for j in range(1,m+1):
        distance[0].append(distance[0][j - 1] + DEL_COST)
    for i in range(1,n+1):
        for j in range(1,m+1):

            distance[i].append(min(
                distance[i-1][j] + INS_COST,
                distance[i-1][j-1] + sub_cost(source[j-1], target[i-1]),
                distance[i][j-1] + DEL_COST
            ))
    return distance[n][m], distance

# TO DO
def computeAlignment(source, target, graph):
    changes = ""
    i = len(graph) - 1
    j = len(graph[0]) - 1

    while i > 0 and j > 0:
        print changes

        value = min(graph[i-1][j-1], graph[i][j-1], graph[i-1][j])
        print "Value:",value
        if value == graph[i-1][j-1]:
            if graph[i][j] == graph[i-1][j-1]:
                changes = " " + changes
            else:
                changes = "s" + changes
            i -= 1
            j -= 1
        elif value == graph[i][j-1]:
            j -= 1
            changes = "d" + changes
        else:
            i -= 1
            changes = "i" + changes

    # now in a 0 row or column, or both
    while j > 0:
        changes = "d" + changes
        j -= 1
    while i > 0:
        changes = "i" + changes
        i -= 1

    print changes



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Incorrect.\nUsage: python proj5.py <source> <target>"
        exit()
    print "Source:", sys.argv[1], "\nTarget:", sys.argv[2]
    distance, graph = minEditDistance(sys.argv[1], sys.argv[2])
    print "Min Edit Distance:", distance
    print graph
    computeAlignment(sys.argv[1], sys.argv[2], graph)
