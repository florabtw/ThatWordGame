wordSet = set(open('words.txt', 'r').read().split())
for word in wordSet:
    word = word.lower()
    letterFile = open('words/' + word[0] + '.csv', 'a')
    letterFile.write(word + '\n')
