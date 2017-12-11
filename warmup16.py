#Andrew Parker
#Dec. 11, 2017
#warmup16.py - find all words in the dictionary that start with your first initial and end with your last initial

#Dictionary Searcher
dictionary = open('engmix.txt')


words = []

for line in dictionary:
    words.append(line.strip())
    

for word in words:
    if word[0] = a and word[-1] = p:
        print word
        