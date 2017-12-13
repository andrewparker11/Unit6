#Andrew Parker
#Dec. 13, 2017
#quiz6
"""
#Program 1 
dictionary = open('engmix.txt')

word = input('Enter a word: ')

words = []

for line in dictionary:
    words.append(line.strip())
    
if word in words:
    print(word, 'is in the dictionary')
else: 
    print(word, 'is not in the dictionary')

#Program 3
number = int(input('Enter a number: ')

"""

"""
#Program 5 

dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())
    
print(words[len(words)/2])
"""

dictionary = open('engmix.txt')

n = [0]*22


for word in dictionary:
    length = len(word.strip())
    
    n[length] = n[length] + 1
    
print(n)

i = 0
x = 1
for num in n:
    if i<23:
        print('There are', n[i], 'words with', x,'letters')
    i = i+1
    x = x+1

