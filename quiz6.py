#Andrew Parker
#Dec. 13, 2017
#quiz6

"""

#Program 4
dictionary = open('engmix.txt')
letter = int(input('Enter a letter: ')

words = []
amount = []

for line in dictionary:
    words.append(line.strip())
    
for word in words:
    if letter not in word:
        amount.append(word)

print(len(amount))

"""


#Program 2 
dictionary = open('engmix.txt')

words = []
amount = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if len(word) > 0:
        if word[0] == 'r':
            amount.append(word)

print(len(amount))




#Program 1 
dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())

for word in words:
    if word.count('c') == 3:
        if word.count('p') == 2:
            print(word)



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


#Program 5 

dictionary = open('engmix.txt')

words = []

for line in dictionary:
    words.append(line.strip())
    
print(words[len(words)/2])
