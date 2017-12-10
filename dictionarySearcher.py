#Andrew Parker
#Dec. 8, 2017

dictionary = open('engmix.txt')

w = input('Enter a word: ')

words = []

for line in dictionary:
    words.append(line.strip())
    
if w in words:
    print(w, 'is in the dictionary')
else: 
    print(w, 'is not in the dictionary')