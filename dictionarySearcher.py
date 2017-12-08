#Andrew Parker
#Dec. 8, 2017

dictionary = open('engmix.txt')

stuff = input('Enter a word: ')

word = []

for line in dictionary:
    word.append(line.strip())
    
if stuff in word:
    print(stuff, 'is in the dictionary')
else: 
    print(stuff 'is not in the dictionary')