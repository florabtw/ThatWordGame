#! /usr/bin/python

import string

userWord = raw_input("Choose a word: ")

print

def wordMatch(baseWord, testWord):
    return False

alphabet = string.ascii_lowercase
validWords = []
# in case the length of the alphabet changes
for i in range(len(alphabet)):
    letter = alphabet[i]

    if letter not in userWord:
        continue

    letterList = open('words/' + letter + '.csv', 'r').read().split()
    for word in letterList:
        if wordMatch(userWord, word):
            validWords.append(word)

print validWords
