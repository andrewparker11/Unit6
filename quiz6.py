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


#Program 2 
dictionary = open('engmix.txt')

for word in dictionary:
    length = len(word.strip())
    word2 = word.strip()
    if length > 0:
        if word[0] == 'r':
print(word2)
        
    


"""
#Program 5 

dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())
    
print(words[len(words)/2])
"""