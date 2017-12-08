#Andrew Parker

dictionary = open('engmix.txt')

stuff = input('Enter a word: ')

word = []

for line in dictionary:
    word.append(line.strip())
    
for w in word:
    if stuff in word:
        print('True')
