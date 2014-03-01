#! /usr/bin/python

import string

alphabet = string.ascii_lowercase

# saving in two places in order to close files at the end
letterFiles = {}
files = []
for letter in alphabet:
    letterFiles[letter] = open('../words/' + letter + '.csv', 'w')
    files.append(letterFiles[letter])

wordSet = set(open('words.txt', 'r').read().split())
for word in wordSet:
    word = word.lower()
    letterFiles[word[0]].write(word + '\n')

for f in files:
    f.close()
