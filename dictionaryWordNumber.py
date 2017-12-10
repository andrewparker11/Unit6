#Andrew Parker
#Dec. 8, 2017

#Dictionary Searcher
dictionary = open('engmix.txt')

word = input('Enter a word: ')

words = []

for line in dictionary:
    words.append(line.strip())
    
if word in words:
    print(word, 'is in the dictionary')
else: 
    print(word, 'is not in the dictionary')



#Dictionary Word Number

dictionary = open('engmix.txt')

num = int(input('Enter a number: '))

word = []

for line in dictionary:
    word.append(line.strip())
    
print(word[num-1])



#File Exclamation Adder
file = open('input.txt')

file2 = []

for line in file:
    file2.append(line.strip())
    file2 + '!'
print(file2)