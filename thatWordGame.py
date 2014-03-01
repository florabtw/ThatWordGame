#! /usr/bin/python

import string

userWord = raw_input("Choose a word: ")

print

def wordMatch(baseWord, testWord):
    if len(testWord) > len(baseWord):
        return False

    for i in range(len(testWord)):
        letter = testWord[i]
        if letter in baseWord:
            baseWord = baseWord.replace(letter, '', 1)
        else:
            return False
    return True

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
