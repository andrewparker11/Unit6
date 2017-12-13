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





"""

#Program 3
dictionary = open('engmix.txt')

number = int(input('Enter a number: '))

words = [] 

for line in dictionary:
    words.append(line.strip())

for word in words:
    if len(word) == number:
        print(word)
        break 







"""
#Program 2 
dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if len(word) > 0:
        if word[0] == 'r':
            print(word)
        
"""   


"""
#Program 5 

dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())
    
print(words[len(words)/2])
"""